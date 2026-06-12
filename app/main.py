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
        ip_address = socket.gethostbyname(host)
        subprocess.call(['ping', ip_address])
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}