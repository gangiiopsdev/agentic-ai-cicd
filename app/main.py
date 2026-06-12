from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.command = ['ping']

    def execute(self, host: str) -> dict:
        command = self.command + shlex.split(host)
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    return safe_ping.execute(host)