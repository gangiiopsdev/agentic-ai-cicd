from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

global_safe_ping = SafePing(None)

def safe_ping(host):
    global_safe_ping.host = host
    return global_safe_ping.execute()

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": safe_ping(host)}