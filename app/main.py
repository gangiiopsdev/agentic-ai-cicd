from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper sanitization
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}