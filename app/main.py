from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper validation
    if not host or not isinstance(host, str):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)