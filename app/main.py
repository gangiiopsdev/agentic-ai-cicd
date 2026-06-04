from fastapi import FastAPI
import subprocess

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        return {"error": "Invalid characters in hostname"}
    status = run_ping(host)
    return {"status": status}