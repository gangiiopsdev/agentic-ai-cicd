from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    return subprocess.run(['ping', host], capture_output=True, text=True, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = run_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}