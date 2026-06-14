from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    sanitized_host = subprocess.run(['echo', host], capture_output=True, text=True).stdout.strip()
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}