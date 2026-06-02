from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use the safe way to call ping without shell=True
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}