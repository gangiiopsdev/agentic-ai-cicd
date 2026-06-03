from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"`
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call with shell=True
        result = subprocess.run(['ping', host], check=True, capture_output=True)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}