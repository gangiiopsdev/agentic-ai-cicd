from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with a list of arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}