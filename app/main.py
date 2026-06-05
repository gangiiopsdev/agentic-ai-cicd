from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host):
        # Safe implementation without shell=True and with basic validation
        if not host or ' ' in host:
            return "Invalid host"
        subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.execute(host)
    if 'Invalid host' in result:
        return {"error": "Invalid host"}, 400
    return {"status": "completed"}