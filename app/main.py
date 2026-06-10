from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and arg splitting
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    if '@' not in host:
        safe_ping(host)
    else:
        raise ValueError('Invalid hostname')
    return {"status": "completed"}