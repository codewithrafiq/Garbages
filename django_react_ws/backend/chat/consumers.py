import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

        await self.channel_layer.gorup_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': '%s has joined the room' % self.room_name
            }
        )

        async def chat_message(self, event):
            message = event['message']

            await self.send(text_data=json.dumps({
                'message': message
            }))

        async def disconnect(self):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name 
            )

        
