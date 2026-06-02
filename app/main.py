from fastapi import FastAPI
import subprocess
class PingHandler:
    @staticmethod
def ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    PingHandler.ping(host)
    return {'status': 'completed'}