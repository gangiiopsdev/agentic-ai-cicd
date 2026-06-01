from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list instead of string
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout.strip(),

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        raise ValueError('Invalid host input')
    status = safe_ping(host)
    return {"status": status}