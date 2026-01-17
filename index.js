import { WebSocketServer } from "ws";

// Railway の環境変数 PORT を使う
const PORT = process.env.PORT || 3000;

const wss = new WebSocketServer({ port: PORT });

wss.on("connection", (ws) => {
  console.log("クライアント接続");
  ws.send("ようこそ wss サーバーへ!");

  ws.on("message", (msg) => {
    console.log("受信:", msg.toString());
    ws.send(`サーバーから返信: ${msg}`);
  });
});

console.log(`WebSocket サーバーが ${PORT} で起動`);
