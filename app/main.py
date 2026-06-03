from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)