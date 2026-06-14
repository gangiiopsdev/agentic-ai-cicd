from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "output": subprocess.run(['ping', host], check=True, capture_output=True).stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}