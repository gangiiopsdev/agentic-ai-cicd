from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.check_call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e)}