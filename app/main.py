from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced security check
    if not host.isalnum() or '<' in host or '>' in host or '&' in host or ';' in host:
        raise ValueError('Invalid hostname')
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}