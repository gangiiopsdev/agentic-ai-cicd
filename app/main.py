from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent injection
        raise ValueError('Invalid input')
    result = subprocess.run(['ping', f'127.0.0.1'], capture_output=True, text=True)  # Use a safe default host
    return {"status": "completed", "output": result.stdout}