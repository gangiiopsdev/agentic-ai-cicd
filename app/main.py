from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if 'ping' in host or any(char in host for char in [';', '|', '&', '*', '?', '$', '`']):
            raise ValueError('Invalid input')
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}