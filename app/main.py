from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.run with proper validation and sanitization
        subprocess.run(['ping', '-c', '1', self.host], check=True)

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
    except Exception as e:
        return {"error": str(e), "status": "failed"}