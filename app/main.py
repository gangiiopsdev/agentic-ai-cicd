from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        raise ValueError('Invalid host name')
    response = PingService.ping(host)
    return {"status": "completed", "response": response}