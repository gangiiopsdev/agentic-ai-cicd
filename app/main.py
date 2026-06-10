from fastapi import FastAPI
import subprocess
def secure_ping(host):
    try:
        output = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)