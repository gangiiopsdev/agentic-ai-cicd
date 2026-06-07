from fastapi import FastAPI
import subprocess
call = subprocess.call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    call(['ping', host])

    return {"status": "completed"}