import base64
import json
import os
import time
import threading
from merlin.celery import app, get_blender
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

@app.task(bind=True, track_started=True)
def render(task, data, reply_channel):
    bpy = get_blender()
    setup_scene(bpy, data)

    context = {'rendering': True, 'filepath': os.path.join(settings.BLENDER_RENDER_TMP_DIR, task.request.id)}
    sync_thread = threading.Thread(target=sync_render, args=(bpy, context, reply_channel))
    sync_thread.start()
    bpy.ops.render.render()
    context['rendering'] = False
    sync_thread.join()

    if os.path.exists(context['filepath']):
        os.remove(context['filepath'])

    if reply_channel is not None:
        async_to_sync(channel_layer.send)(reply_channel, {
            'text': json.dumps({
            'action': 'render_finished'
        })
    })

def setup_scene(bpy, data):
    try:
        levels = int(data['subsurf'])
    except ValueError:
        levels = 0
    bpy.context.object.modifiers[0].render_levels = levels

def sync_render(bpy, context, reply_channel):
    while context['rendering']:
        time.sleep(settings.BLENDER_RENDER_SYNC_INTERVAL)

        image = bpy.data.images['Render Result']
        image.save_render(filepath=context['filepath'])

        with open(context['filepath'], "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        if reply_channel is not None:
            async_to_sync(channel_layer.send)(reply_channel, {
            'text': json.dumps({
            'action': 'render_finished'
        })
    })
