from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate the host input to ensure it is safe for the ping command
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "result": result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe for the ping command
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "result": result.stdout}