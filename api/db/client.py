import asyncio
from websockets.sync.client import connect
import websockets
import json
import user
from user import user

#cliente precisa ficar "online" p/ receber dara e hora a cada segundo
#fazer um boolean pro cliente ser identificado como on ou offline
#transformar a chave nome em chave candidata
#cliente precisa receber isoladamente o retorno de fibonacci caso envie um número como requisição
#criar um if para perguntar se o nome (unique) já existe e caso não criar no banco de dados


def hello():
    name = input("insira seu nome ")
    x=user(name)
    y=json.dumps(x.__dict__)
    print(y)
    
    with connect("ws://localhost:6687") as websocket:
      
        websocket.send(x.nome)
        while(True):
            message = websocket.recv()
            print(f"Received: {message}")
hello()

async def main():
            
                    await asyncio.Future()  # run forever
asyncio.run(main())