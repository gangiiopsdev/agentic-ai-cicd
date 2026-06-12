from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}