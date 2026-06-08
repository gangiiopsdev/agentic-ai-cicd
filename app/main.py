from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "Success", "output": result.stdout}
    else:
        return {"status": "Failure", "output": result.stderr}