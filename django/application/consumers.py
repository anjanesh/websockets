from channels.generic.websocket import AsyncWebsocketConsumer 
# from asgiref.sync import async_to_sync
import time, asyncio

class TerraformUpdates(AsyncWebsocketConsumer):
    
    def __init__(self):
        self.i = 0
        print("init done")
        self.groups = ["room1", "room2"]        

    async def connect(self):        

        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")

    async def receive(self, text_data):
        print("Received : " + text_data)
        if (text_data == "START"):        
            await self.send_message(self)

    async def send_message(self, res):       
        # Send message to WebSocket
        for j in range(0, 10):
            self.i = self.i + 1
            await asyncio.sleep(1)
            await self.send(text_data=f"Person : {self.i}")
        await self.send(text_data="DONE")
        
        