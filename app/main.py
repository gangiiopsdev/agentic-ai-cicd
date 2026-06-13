from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation using shlex.quote to escape arguments
        import shlex
        safe_host = shlex.quote(host)
        subprocess.call(f'ping {safe_host}', shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}