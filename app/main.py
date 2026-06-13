from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        try:
            args = shlex.split(f'ping {self.host}')
            result = subprocess.run(args, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    return safe_ping.ping()