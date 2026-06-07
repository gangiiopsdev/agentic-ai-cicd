from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or 'ping' in host:
        return False
    try:
        # Sanitize the host input to prevent command injection
        safe_host = subprocess.quote(host)
        subprocess.run(['ping', safe_host], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid input or error during ping"}