from fastapi import FastAPI
import subprocess
from shlex import quote

class SafeSubprocess:
    @staticmethod
def run(command: list[str]):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    safe_host = quote(host)
    command = ['ping', safe_host]
    return SafeSubprocess.run(command)