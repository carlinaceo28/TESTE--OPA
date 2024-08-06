import asyncio
from websockets.sync.client import connect
import websockets
import json
import user
from user import user


def hello():
    x=user("maria")
    y=json.dumps(x.__dict__)
    print(y)
    
    with connect("ws://localhost:6687") as websocket:
      
        websocket.send(y)
        message = websocket.recv()
        print(f"Received: {message}")
hello()

async def main():
            
                    await asyncio.Future()  # run forever
asyncio.run(main())