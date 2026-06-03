from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with list arguments and shell=False
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
        return {"status": "completed", "output": status}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}