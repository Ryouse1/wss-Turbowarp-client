import asyncio
import websockets
import json

async def send_score(score):
    uri = "wss://wss-turbowarp-client-network.up.railway.app"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"score": score}))

asyncio.run(send_score(42))
