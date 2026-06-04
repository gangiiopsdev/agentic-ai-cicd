from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Validate and sanitize the host parameter
    if not host.isalnum():
        return 'Invalid input'
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)