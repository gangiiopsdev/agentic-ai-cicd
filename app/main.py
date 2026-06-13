from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not all(c.isalnum() for c in host):  # Basic validation, improve as needed
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}