from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}

def validate_host(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    return host in allowed_hosts