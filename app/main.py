from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed', 'output': ''}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.stderr}