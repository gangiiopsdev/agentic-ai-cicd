from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        if 'ping' in host or any(char.isalnum() for char in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        command = ['ping', shlex.quote(host)]
        try:
            output = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    return SafePing.ping(host)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}