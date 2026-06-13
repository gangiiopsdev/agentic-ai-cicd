from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Safer implementation using subprocess.run with shell=False and arguments split
            args = shlex.split(f'ping {host}')
            result = subprocess.run(args, check=True, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': 'Ping failed', 'message': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)