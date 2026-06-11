from fastapi import FastAPI
import socketio

app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')
app.mount('/socket.io', sio)

@sio.on('ping')
def ping(sid, data):
    return {'status': 'completed'}