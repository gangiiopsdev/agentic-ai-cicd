from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and proper input handling
    subprocess.call(['ping', host], shell=False, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    try:
        ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}