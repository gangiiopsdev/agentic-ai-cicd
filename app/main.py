from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}