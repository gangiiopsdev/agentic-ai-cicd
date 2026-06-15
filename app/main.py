from fastapi import FastAPI
import subprocess
given_host = '127.0.0.1' # replace this with a safe default value or validation logic

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using subprocess.run with a whitelist of allowed hosts
    if host in ['127.0.0.1', '::1']: # replace this with your actual validation logic
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}