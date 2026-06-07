from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run for a safer implementation with full path and input validation
        if not host.isalnum() or len(host) > 255:
            raise ValueError('Invalid hostname')
        result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}