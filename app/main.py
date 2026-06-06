from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = Ping().ping_command + [host]
    subprocess.call(ping_command)
    return {"status": "completed"}