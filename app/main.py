from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    safe_host = host.replace('.', '_').replace('-', '_')  # Simple sanitization
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}