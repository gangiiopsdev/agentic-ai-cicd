from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, host):
        self.host = host

    def safe_ping(self):
        args = shlex.split(f'ping {shlex.quote(self.host)}')
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping_instance = SafePing(host)
    result = safe_ping_instance.safe_ping()
    return {'status': 'completed', 'output': result.stdout}