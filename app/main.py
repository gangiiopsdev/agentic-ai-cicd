from fastapi import FastAPI
import subprocess
def ping(host: str):
    cmd = ['ping', '-c', '1', host]
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    return ping(host)