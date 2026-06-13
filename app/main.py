from fastapi import FastAPI
import subprocess
gl = globals()
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {"status": "failed", "reason": "Invalid host"}
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation, can be expanded
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts