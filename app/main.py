from fastapi import FastAPI
import subprocess
def ping_safe(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ping_safe(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}