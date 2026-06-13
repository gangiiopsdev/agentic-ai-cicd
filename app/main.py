from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize input to prevent command injection
        if '.' in host or not host.isalnum():
            raise ValueError('Invalid host format')
        args = ['ping', '--'] + [host]  # Use '--' before the host parameter to protect against command injection
        result = subprocess.run(args, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    return SafePing.ping(host)