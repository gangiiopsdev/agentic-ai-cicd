from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_ping(subprocess.run(['echo', host], capture_output=True, text=True).stdout.strip())
    return {"status": "completed"}