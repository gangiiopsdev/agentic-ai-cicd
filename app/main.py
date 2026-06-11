from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use a full path for the ping executable to avoid potential issues
        output = subprocess.run(['/usr/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

global app
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}