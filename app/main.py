from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate host to ensure it's a safe hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname or IP address')
        command = ['ping', *shlex.split(host)]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}