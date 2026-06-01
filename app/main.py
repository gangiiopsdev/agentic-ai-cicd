from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Enhanced implementation using subprocess.run with shell=False and args parameter, and validating the host input
        if not host or ' ' in host or '.' not in host:
            return {"error": "Invalid host"}
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}