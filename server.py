import asyncio
import websockets
import json
import os

connected = set()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            # 接続中の全員に送信
            for conn in connected:
                await conn.send(json.dumps(data))
    finally:
        connected.remove(websocket)

async def main():
    port = int(os.environ.get("PORT", 8765))  # Render が自動で PORT を指定
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"WebSocket server started on port {port}")
        await asyncio.Future()  # 永久に実行

asyncio.run(main())
