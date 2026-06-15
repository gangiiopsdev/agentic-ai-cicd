from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Validate input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)