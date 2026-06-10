from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not all(c.isalnum() or c in '.-' for c in host):
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}