from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    safe_ping(host)
    return {"status": "completed"}