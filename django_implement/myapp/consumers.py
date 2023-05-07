import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["content"]
        self.send(
            text_data=json.dumps(
                {
                    "type": "chat.message",
                    "sender": "John",
                    "content": message,
                    "timestamp": str(datetime.now()),
                }
            )
        )
