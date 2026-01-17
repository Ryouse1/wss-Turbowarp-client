import asyncio
import websockets
import json

async def send_score(value):
    uri = "wss://your-project.onrender.com"  # Render の URL に置き換え
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"score": value}))

# 例：Gemini で生成した値を送信
score_value = 42
asyncio.run(send_score(score_value))
