from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    # Sanitize input to prevent command injection
    host = shlex.quote(host)
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

class PingService:
    @staticmethod
def validate_host(host: str) -> bool:
        # Basic validation of the hostname
        return all(c.isalnum() or c in '-.' for c in host)

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if PingService.validate_host(host):
        return run_ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid host name'}