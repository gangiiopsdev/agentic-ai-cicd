from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() and not host.strip().startswith('-'):  # Avoid common flags for ping
        try:
            subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "message": "Ping successful"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "message": str(e)}
    else:
        return {"status": "invalid_host", "message": "Invalid host or flag provided"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)