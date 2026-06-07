from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {"status": "completed"}