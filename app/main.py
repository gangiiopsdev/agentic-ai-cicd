from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.ping_commands = ['ping -c 1', 'ping -4 -c 1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ["example.com", "another-example.com"]:
        raise Exception("Invalid host")

    # Safe implementation with validation and sanitization
    command = PingCommand().ping_commands[0]
    subprocess.call(command.split())

    return {"status": "completed"}