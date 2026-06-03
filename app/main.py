from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}