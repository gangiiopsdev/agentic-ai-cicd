from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the input more strictly
        if host not in ['127.0.0.1', 'localhost']:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts or validate the input more strictly
    if host not in ['127.0.0.1', 'localhost']:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)