from fastapi import FastAPI
import subprocess
call_subprocess = subprocess.run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    call_subprocess(['ping', host], check=True)
    return {"status": "completed"}