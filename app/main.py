from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}