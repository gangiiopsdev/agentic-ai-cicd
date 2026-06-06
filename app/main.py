from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    allowed_hosts = ["example.com", "test.com"]
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail="Invalid host")
    subprocess.run(['ping', host], shell=False, check=True)
    return {"status": "completed"}