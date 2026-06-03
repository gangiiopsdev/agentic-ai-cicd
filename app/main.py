from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError("Invalid input")
    return PingService.ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}