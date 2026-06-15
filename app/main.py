from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['safehost1', 'safehost2']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.run(['ping', host], check=True, capture_output=True)  # Use run instead of call
    return {"status": "completed"}