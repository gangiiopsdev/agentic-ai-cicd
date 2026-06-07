from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.command = 'ping'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run([PingCommand().command, host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode()}, 500