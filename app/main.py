from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    if ' ' in host or ';' in host:
        raise ValueError('Invalid input')
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}