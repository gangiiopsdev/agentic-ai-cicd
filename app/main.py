from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid hostname"}, 400
    result = PingCommand.execute(host)
    return {"status": result.stdout}