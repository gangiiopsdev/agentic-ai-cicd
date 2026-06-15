from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/""
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation for host
    if not host or len(host) > 255:
        return {"error": "Invalid input for host"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}