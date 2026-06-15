from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping'], capture_output=True, text=True, input=host)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)