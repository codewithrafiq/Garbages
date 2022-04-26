from fastapi import FastAPI,WebSocket


app  = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("websocket_endpoint")
    await websocket.accept()
    await websocket.send_text("Hello World")
    print('Accepted')
    while True:
        try:
            print('waiting')
            msg = await websocket.receive_text()
            print(msg)
            await websocket.send_text(msg)
            print('sent')
        except:
            print('error')
            break
    await websocket.close()