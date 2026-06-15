from fastapi import FastAPI
import subprocess
import shlex
import os

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']

    def validate_host(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')

    def execute_ping(self, host: str):
        args = shlex.split(f'ping {host}')
        subprocess.run(['ping', '-c', '1', host], check=True)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get(")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.validate_host(host)
    safe_ping_instance.execute_ping(host)
    return {'status': 'completed'}