from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate the host to ensure it does not contain malicious content
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it does not contain malicious content
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return result.stdout