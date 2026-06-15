from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.strip():
            return False
        args = ['ping', '--'] + list(filter(None, host.split(' ')))
        result = subprocess.run(args, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)