from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = host.strip().replace(' ', '_')
    if not safe_host:
        raise ValueError("Invalid input")
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}