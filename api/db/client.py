import asyncio
from websockets.sync.client import connect
import websockets
import json
import user
from user import user
import keyboard
from datetime import datetime
#cliente precisa ficar "online" p/ receber dara e hora a cada segundo
#fazer um boolean pro cliente ser identificado como on ou offline
#transformar a chave nome em chave candidata
#cliente precisa receber isoladamente o retorno de fibonacci caso envie um número como requisição
#criar um if para perguntar se o nome (unique) já existe e caso não criar no banco de dados

#def keyhandler():
   # while(true):
     #      if keyboard.is_pressed:
                  
def is_datetime(message):
# initializing string
    test_str = message

# printing original string
    #print("The original string is : " + str(test_str))

# initializing format 
    format = "%Y-%m-%d %H:%M:%S"

# checking if format matches the date 
    res = True

# using try-except to check for truth value
    try:
        res = bool(datetime.strptime(test_str, format))
    except ValueError:
        res = False
    return res
# printing result
#print("Does date match format? : " + str(res))








def hello():
    print("Para visualizar o Date_Time matenha pressionado ctrl")
    name = input("insira seu nome ")

    x=user(name)
    y=json.dumps(x.__dict__)
    print(y)
    
    with connect("ws://localhost:6687") as websocket:
      
        websocket.send(x.nome)
        while(True):
            message = websocket.recv()
            if (not is_datetime(message)) or (keyboard.is_pressed("ctrl")) : 
                print(f"Received: {message}")

hello()

async def main():
            
                    await asyncio.Future()  # run forever
asyncio.run(main())