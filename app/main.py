from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = shlex.split(f'ping {host}')
            result = subprocess.run(args, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    safe_pinger = SafePing()
    return {'status': 'completed', 'output': safe_pinger.ping(host)}