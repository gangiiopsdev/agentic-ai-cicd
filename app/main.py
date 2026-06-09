from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if host.isnumeric() and len(host) <= 15:
        subprocess.call(["ping", host])