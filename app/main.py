from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        subprocess.run(['ping', '-c', '1', host], check=True, timeout=5)
        return {"status": "completed", "result": "Success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "result": str(e)}

# Recommended improvements:
# 1. Use a whitelist of allowed hosts.
# 2. Sanitize or validate the input host parameter more strictly.