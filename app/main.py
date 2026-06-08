from fastapi import FastAPI
import ipaddress
import shlex
import subprocess

global_ping_hosts = {'example.com', 'localhost'}

class PingService:
    @staticmethod
    def ping(host: str):
        try:
            ipaddress.ip_address(host)
        except ValueError:
            raise ValueError('Invalid host')
        if host in global_ping_hosts:
            command = ['ping', '-c', '1', shlex.quote(host)]
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    result = PingService.ping(host)
    return {'status': 'completed', 'output': result}