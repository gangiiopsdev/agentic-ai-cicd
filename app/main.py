from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run with list of arguments for safety
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}