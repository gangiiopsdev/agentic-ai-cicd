from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.call(args)
        return {'status': 'completed', 'result': result}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return SafePing.ping(host)