from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        socket.create_connection((host, 80), timeout=2)
        return {'status': 'completed', 'result': 'Ping successful'}
    except (socket.gaierror, socket.timeout):
        return {'status': 'completed', 'result': 'Ping failed'}
    except Exception as e:
        return {'status': 'completed', 'result': str(e)}