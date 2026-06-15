from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run()
    cmd = ['ping', host]
    for arg in cmd:
        if isinstance(arg, str) and '\' in arg:
            raise ValueError('Invalid input detected')
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}