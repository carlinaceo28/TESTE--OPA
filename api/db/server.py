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
        self.connected = []

#função que retorna a sequência de Fibonacci até o enésimo termo (n).
    def fibonacci(self,n):
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
        return seq[-1]
        
    def run_server(self):
            async def handler(websocket):
               await asyncio.gather(
                    Enviar_timer(websocket),
                    Processar_Dados(websocket)
                )

            async def registrar_nome(websocket):
                async for message in websocket:
                    print(message) #comando para mandar p/ o banco.sql
                    #if message for user add no banco via websocket
                    self.db.add_user(message)
                    #if message for um N devolver fibonacci
                    if (websocket not in self.connected):
                        self.connected.append(websocket)
                    websockets.broadcast(self.connected,message)    
            
            async def Enviar_timer(websocket):     
               while(True):
                hour= datetime.now().isoformat(" ","seconds")
                await websocket.send(hour)
                await asyncio.sleep(1)

            def Processar_Fibonacci(number):
                        total= self.fibonacci(number)
                        return str(total)
                        
            async def Processar_Dados(websocket):
                async for message in websocket:
                    try: 
                        value = int(message)
                        total = Processar_Fibonacci(value)
                        await websocket.send(total)
                    except ValueError:
                        registrar_nome(message)



            async def main():
                async with serve(handler, "localhost", self.port):    
                    await asyncio.Future()  # run forever
             
            asyncio.run(main())

  

