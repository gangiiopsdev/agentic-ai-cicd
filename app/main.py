from fastapi import FastAPI
import socketio

app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')
app.mount('/', sio)

async def ping(host: str):
    try:
        with socketio.Client() as client:
            await client.ping(host)
            return {'result': 'Success'}
    except socketio.exceptions.ConnectionError as e:
        return {'result': 'Failure', 'error': str(e)}

@sio.on('connect')
def connect(sid, environ):
    print(f'Client {sid} connected')