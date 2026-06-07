from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts