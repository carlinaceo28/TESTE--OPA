import asyncio
from websockets.sync.client import connect
import websockets
import json
import user
from user import user


def hello():
    x=user("Carlos",12)
    y=json.dumps(x.__dict__)
    print(y)
    
    with connect("ws://localhost:6687") as websocket:
      
        websocket.send(y)
        message = websocket.recv()
        print(f"Received: {message}")
hello()