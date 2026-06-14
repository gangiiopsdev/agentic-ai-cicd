from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Sanitize the input to prevent command injection
        safe_host = host.replace(';', '').replace('&', '')
        return subprocess.run(['ping', safe_host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.execute(host)
    return {"status": "completed", "output": result.stdout}