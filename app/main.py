from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'github.com']  # Example allowed hosts

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid hostname')
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, check=True)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
safe_ping_instance.safe_ping(host)
return {"status": "completed"}