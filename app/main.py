from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError('Unauthorized host')
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts