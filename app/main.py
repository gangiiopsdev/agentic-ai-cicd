from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Define a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)