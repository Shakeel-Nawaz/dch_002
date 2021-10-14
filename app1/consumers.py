from channels.generic.websocket import AsyncWebsocketConsumer
import json
from time import sleep

from app1.views import cheek

class AsycConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'nawaz'
        self.room_group_name = 'home'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        for i in range(10,110,10):
            abd = cheek(i)
            await self.channel_layer.group_send(
            'home',{
                'type': 'checkfunc',    
                'value': abd
                })

    
    async def receive(self, text_data=None, bytes_data=None, **kwargs): pass

    async def close(self, code=None): pass

    async def checkfunc(self,even):
        message = even['value']
        xya = json.dumps({
            'message': str(message)
        })
        sleep(0.5)
        # Send message to WebSocket
        await self.send(text_data=xya)

