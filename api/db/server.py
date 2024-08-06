import asyncio
from websockets.server import serve
from websockets.sync.client import connect
import websockets
from db.connections import db_connector

class db_server:
    def __init__(self,port):
        self.db = db_connector()
        self.port = port
        
    def run_server(self):
            async def echo(websocket):
                async for message in websocket:
                    print(message) #comando para mandar p/ o banco.sql
                    self.db.add_user(message)
                    await websocket.send(message)

        
            async def main():
                async with serve(echo, "localhost", self.port):
                    await asyncio.Future()  # run forever
            asyncio.run(main())

  

