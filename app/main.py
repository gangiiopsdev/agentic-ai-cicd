from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Invalid host provided')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)