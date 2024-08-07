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

#função que retorna o somatório de uma sequência de Fibonacci até o enésimo termo (n).
    def fibonacci_sum_recursive(self,n):
        num1 = 0
        num2 = 1
        next_number = num2 
        count = 1
        if n<=1:
            return n
        while count <= n:
            count += 1
            num1, num2 = num2, next_number
            next_number = num1 + num2
        return num1
        
    def run_server(self):
            async def handler(websocket):
               await asyncio.gather(
                    Enviar_timer(websocket),
                    Processar_Dados(websocket)
                    #registrar_nome(websocket,message)
                )

            async def registrar_nome(websocket,message):

                    print(message) #comando para mandar p/ o banco.sql
                    #if message for user add no banco via websocket
                    self.db.add_user(message)
                    #if message for um N devolver fibonacci
                    if (websocket not in self.connected):
                        self.connected.append(websocket)
                    #websockets.broadcast(self.connected,message)    
            
            async def Enviar_timer(websocket):     
               while(True):
                hour= datetime.now().isoformat(" ","seconds")
                await websocket.send(hour)
                await asyncio.sleep(1)

            def Processar_Fibonacci(number):
                        print(type(number))
                        total = self.fibonacci_sum_recursive(number)
                        
                        return str(total)
                        
            async def Processar_Dados(websocket):
                
                async for message in websocket:
                    try: 
                        value = int(message)
                        #print(value)
                        total = Processar_Fibonacci(value)

                        await websocket.send(total)
                    except ValueError:
                        #print(message)
                        await registrar_nome(websocket,message)



            async def main():
                async with serve(handler, "localhost", self.port):    
                    await asyncio.Future()  # run forever
             
            asyncio.run(main())

  

