from fastapi import FastAPI
import subprocess
global ping_count
ping_count = 0

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_count
    ping_count += 1
    if ping_count > 5:
        raise Exception("Too many pings")
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}