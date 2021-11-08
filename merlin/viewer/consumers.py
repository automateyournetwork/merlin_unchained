import json
from celery import group
from channels import Channel
from channels.sessions import channel_session
from .tasks import render


@channel_session
def ws_connect(message):
    message.reply_channel.send({
        "text": json.dumps({
            "action": "reply_channel",
            "reply_channel": message.reply_channel.name,
        })
    })


@channel_session
def ws_receive(message):
    try:
        data = json.loads(message['text'])
    except ValueError:
        return

    if data:
        reply_channel = message.reply_channel.name

        if data['action'] == "start_render":
            start_render(data, reply_channel)


def start_render(data, reply_channel):
    task = render.delay(data, reply_channel)
    Channel(reply_channel).send({
        "text": json.dumps({
            "action": "started",
            "task_id": task.id
        })
    })