from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Input validation to prevent command injection
    if not host.strip().isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation to prevent command injection
    if not host.strip().isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)