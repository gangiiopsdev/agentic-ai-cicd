from fastapi import FastAPI
import subprocess
import re
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    return SafePing.ping(host)