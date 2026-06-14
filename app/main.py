from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

class SafePing:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts if allowed_hosts else []

    def validate_host(self, host):
        return host in self.allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing(allowed_hosts=['127.0.0.1', 'localhost'])  # Define allowed hosts
    if not safe_ping_instance.validate_host(host):
        return {"status": "error", "response": "Host is not allowed"}
    response = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "response": response.stdout}