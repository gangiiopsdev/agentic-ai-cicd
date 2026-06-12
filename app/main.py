from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}