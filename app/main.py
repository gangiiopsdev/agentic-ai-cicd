from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use the list form for subprocess to avoid shell injection
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}