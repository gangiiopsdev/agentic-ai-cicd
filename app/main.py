from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with shell=False
        subprocess.run(['ping', self.host], check=True)

global_safe_ping = SafePing('default_host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing(host)
    safe_ping_instance.execute()
    return {"status": "completed"}