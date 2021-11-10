import json
from channels.generic.websocket import WebsocketConsumer
from .tasks import render

class Monkey(WebsocketConsumer):
    def connect(self, message):
        self.accept({
           "type": "websocket.accept",
           "text": json.dumps({
           "action": "reply_channel",
           "reply_channel": message.reply_channel.name,
            })
        })

    def receive(self, message, event):
        try:
            data = json.loads(message['text'])
        except ValueError:
            return

        if data:
            reply_channel = message.reply_channel.name

        if data['action'] == "start_render":
            def start_render(self, data, reply_channel):
                task = render.delay(data, reply_channel)
                self.send({
                    "text": json.dumps({
                    "action": "started",
                    "task_id": task.id
                })
            })              
            start_render(data, reply_channel)

        self.send({
            "type": "websocket.send",
            "text": event["Render Finished"],
        })
    
    def disconnect(self, message):
        pass        