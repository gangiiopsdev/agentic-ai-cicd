from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using subprocess.run with a list of arguments instead of a single string.
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    ping_safe(host)
    return {"status": "completed"}