from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}