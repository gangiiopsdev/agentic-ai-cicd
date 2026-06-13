from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)
    return {"status": "completed"}