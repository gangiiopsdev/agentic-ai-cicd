from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.command = ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isnumeric() and len(host.split('.')) != 4:
        return {"error": "Invalid host"}, 400
    ping_instance = PingCommand(host)
    subprocess.call(ping_instance.command)

    return {"status": "completed"}