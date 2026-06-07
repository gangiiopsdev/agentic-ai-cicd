from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Validate the host to ensure it does not contain any potentially dangerous characters
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)