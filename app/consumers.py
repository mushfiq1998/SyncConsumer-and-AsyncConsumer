# Topic - More on consumer and routing
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket connected...........', event)
        # Send request to server to accept connection
        self.send({
            'type': 'websocket.accept'
        }) 
    
    # Server accept data from client
    def websocket_receive(self, event):
        print('Message received from client', event)
        print('Message: ', event['text'])
        # Send data to client from server
        self.send({
            'type': 'websocket.send'
            'text': 'Message sent to client'
        })
    
    def websocket_disconnect(self, event):
        print('websocket disconnected........', event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('websocket connected...........', event)
        # Send request to server to accept connection
        await self.send({
            'type': 'websocket.accept'
        }) 
    
    # Server accept data from client
    async def websocket_receive(self, event):
        print('Message received from client', event)
        print('Message: ', event['text'])
        # Send data to client from server
        await self.send({
            'type': 'websocket.send'
            'text': 'Message sent to client'
        })
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected........', event)
        raise StopConsumer()
