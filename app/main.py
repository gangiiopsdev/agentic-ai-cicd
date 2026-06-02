from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.execute()
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}