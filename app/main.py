from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {"error": "Invalid host"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)