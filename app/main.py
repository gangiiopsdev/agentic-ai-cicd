from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        ping_command = ['ping', host]
        result = subprocess.run(ping_command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        return SafePing.safe_ping(safe_host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}