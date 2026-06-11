from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}