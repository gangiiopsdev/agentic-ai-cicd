from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using Popen instead of call
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}