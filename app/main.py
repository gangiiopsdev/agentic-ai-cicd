from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', 'example.com']  # Fixed to use a known safe host

global_ping_command = PingCommand(host='example.com')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping():
    global_ping_command.execute()
    return {"status": "completed"}