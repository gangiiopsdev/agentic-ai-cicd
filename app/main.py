from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError("Invalid hostname")
        args = ['ping', '127.0.0.1']  # Replace with a fixed or sanitized value
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', '127.0.0.1']  # Replace with a fixed or sanitized value
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout