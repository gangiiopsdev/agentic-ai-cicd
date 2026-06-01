from fastapi import FastAPI
import subprocess

app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.isalnum():  # Simple validation to ensure the input is alphanumeric
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid hostname"}