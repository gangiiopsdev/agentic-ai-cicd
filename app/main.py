from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    allowed_hosts = ["google.com", "example.com"]  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail="Invalid host")
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}