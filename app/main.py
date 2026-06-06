from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not validate_host(host):
        return False
    subprocess.call(['ping', host])

    def validate_host(host: str) -> bool:
        # Simple validation example, replace with a more robust solution
        allowed_hosts = ['example.com', 'localhost']
        return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid host"}