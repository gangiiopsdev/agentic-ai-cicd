from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip().endswith('localhost') or host.strip() == '127.0.0.1':
        return subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        return {"status": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e)}/