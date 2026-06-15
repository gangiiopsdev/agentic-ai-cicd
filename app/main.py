from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def call(host: str):
        command = ['ping', host]
        subprocess.call(command)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing.call(host)
    return {'status': 'completed'}