import asyncio
from websockets.server import serve
from websockets.sync.client import connect
import websockets
from db.connections import db_connector
from datetime import datetime


class db_server:
    def __init__(self,port):
        self.db = db_connector()
        self.port = port
        self.websockets = []
        
    def run_server(self):
            async def echo(websocket):
                async for message in websocket:
                    print(message) #comando para mandar p/ o banco.sql
                    #if message for user add no banco via websocket
                    self.db.add_user(message)
                    #if message for um N devolver fibonacci
                    if (websocket not in self.websockets):
                        self.websockets.append(websocket)
                    for ws in self.websockets:
                        await ws.send(message)

                    
            async def main():
                async with serve(echo, "localhost", self.port):
                    await asyncio.Future()  # run forever
            asyncio.run(main())

  


#função que retorna a sequência de Fibonacci até o enésimo termo (n).
    def fibonacci(n):
        if n <= 0:
            return "O número deve ser maior que zero."
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
         seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq