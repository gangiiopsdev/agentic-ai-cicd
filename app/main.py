from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def run_safe_ping(host):
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.run_safe_ping(host)