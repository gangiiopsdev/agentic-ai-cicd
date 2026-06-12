from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and not '-' in host:
        raise ValueError("Invalid host name")
    output = execute_ping(host)
    return {"status": "completed", "output": output}