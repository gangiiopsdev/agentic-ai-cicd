from fastapi import FastAPI
import subprocess

class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        # Validate and sanitize the input
        allowed_hosts = ['localhost', '127.0.0.1']
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        command = ['ping', host]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.stderr}
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafeSubprocess.safe_ping(host)