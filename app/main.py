from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using list of args
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Using safe function
    safe_ping(host)
    return {"status": "completed"}