from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    # Add input validation for 'host'
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(args, check=True)

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}