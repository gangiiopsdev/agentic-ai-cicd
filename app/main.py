from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    args = ['ping', '-c', '1', host]
    return subprocess.run(args, check=True, capture_output=True)
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout.decode()}