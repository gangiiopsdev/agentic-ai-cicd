from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], check=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing.ping(shlex.quote(host))
    return {'status': 'completed'}