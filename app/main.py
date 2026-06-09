from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list instead of shell=True
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        return {"status": "failed", "result": "Invalid host name"}
    if safe_ping(host.strip()):
        return {"status": "completed", "result": "Ping successful"}
    else:
        return {"status": "failed", "result": "Ping failed"}