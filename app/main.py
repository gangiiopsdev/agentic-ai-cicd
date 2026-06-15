from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        if host not in ['127.0.0.1', 'localhost']:
            raise ValueError('Host is not allowed')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
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
    try:
        response = safe_ping_instance.safe_ping(host)
        return {"status": "completed", "response": response}
    except ValueError as e:
        return {"status": "error", "response": str(e)}