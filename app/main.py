from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_fixed(host: str):
    # Sanitize input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    return {"status": "failed", "reason": "Host not allowed"}