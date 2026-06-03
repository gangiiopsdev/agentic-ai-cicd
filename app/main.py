from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True, capture_output=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {"status": "completed", "output": result.stdout.decode()}