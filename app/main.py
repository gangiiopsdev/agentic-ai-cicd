from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'response': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    return safe_ping(host)