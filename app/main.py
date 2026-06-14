from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in '.-\' for c in host):
            return 'Invalid hostname'
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_handler(host: str):
    return PingService.ping(host)