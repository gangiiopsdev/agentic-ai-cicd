from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}