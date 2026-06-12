from fastapi import FastAPI
import subprocess
import shlex
import os
import re

class SafePing:
    @staticmethod
def ping(host: str) -> dict:
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'invalid_host'}
        # Use a whitelist of allowed hosts or use a more robust validation method
        allowed_hosts = ['example.com', 'another-example.com']
        if host not in allowed_hosts:
            return {'status': 'invalid_host'}
        command = ['ping', shlex.quote(host)]
        try:
            subprocess.check_call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)