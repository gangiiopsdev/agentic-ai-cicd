from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not host.isalnum() or '.' in host:
        return {"error": "Invalid input"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}