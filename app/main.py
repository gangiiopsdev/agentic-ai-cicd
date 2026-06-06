from fastapi import FastAPI
import socketio

sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio)

ALLOWED_HOSTS = ['127.0.0.1', '::1']

@sio.on('ping')
def ping(sid, host: str):
    if host in ALLOWED_HOSTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, 80))
            return {'status': 'completed', 'result': result}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        raise ValueError('Host not allowed')