from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.run with shell=False
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = Ping(host)
    return ping_command.execute()