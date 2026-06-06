from fastapi import FastAPI
import subprocess
import ipaddress
global_ping_hosts = {'example.com', 'localhost'}

class PingService:
    @staticmethod
def ping(host: str):
        try:
            ipaddress.ip_address(host)
        except ValueError:
            raise ValueError('Invalid host')
        if host in global_ping_hosts:
            subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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