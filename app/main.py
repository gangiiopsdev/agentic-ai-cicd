from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and input validation
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True)
    return result.stdout.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent code injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    output = safe_ping(host)
    return {"status": "completed", "output": output}