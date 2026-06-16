from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command: list):
        self.command = command

    def execute(self):
        subprocess.run(self.command)

app = FastAPI()

def ping(host: str):
    # Secure implementation
    PingCommand(['ping', host]).execute()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}