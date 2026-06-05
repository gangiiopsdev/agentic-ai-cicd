from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip() or ' ' in host:
        return {"error": "Invalid input"}, 400
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}