from fastapi import FastAPI
import socketio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')
app.mount('/socket.io', sio)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

cors_middleware = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@sio.on('ping')
def ping(sid, data):
    return {'status': 'completed'}