from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate host input to prevent command injection
        if not host.replace('.', '').isalnum():
            raise ValueError('Invalid host name')
        return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
global_safe_ping = SafePing()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = global_safe_ping.safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except ValueError as e:
        return {"status": "error", "message": str(e)}