from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        ping_command.execute()
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}