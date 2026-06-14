from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {"example.com", "localhost", "127.0.0.1"}

def safe_ping(host):
    if host in globally_allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.stderr}
    else:
        return {'status': 'invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)