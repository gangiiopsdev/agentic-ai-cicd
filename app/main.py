from fastapi import FastAPI
import subprocess
global_ping_hosts = {'example.com', 'localhost'}

class PingService:
    @staticmethod
def ping(host: str):
        if host in global_ping_hosts:
            subprocess.call(['ping', host])
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    PingService.ping(host)
    return {'status': 'completed'}