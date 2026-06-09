from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation with shell=False to avoid command injection
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)