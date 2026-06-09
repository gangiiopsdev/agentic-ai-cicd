from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    result = ping_command.execute()
    if '127.0.0.1' not in result and 'localhost' not in result:
        return {"status": "Unauthorized access attempt detected", "error": "Access denied"}
    else:
        return {"status": result}