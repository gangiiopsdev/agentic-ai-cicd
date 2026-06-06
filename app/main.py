from fastapi import FastAPI
import subprocess
global_ping_hosts = {'example.com', 'localhost'}

class PingService:
    @staticmethod
def ping(host: str):
        if host in global_ping_hosts:
            # Use subprocess.run with shell=False and check=True to prevent command injection
            subprocess.run(['ping', host], shell=False, check=True)
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    PingService.ping(host)
    return {'status': 'completed'}