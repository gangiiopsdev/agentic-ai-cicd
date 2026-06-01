from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)