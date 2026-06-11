from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = ['ping', 'example.com']  # Replace with a safe default value or parameter validation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host == 'example.com':  # Replace with proper validation logic
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "Invalid input", "error": "Only 'example.com' is allowed"}