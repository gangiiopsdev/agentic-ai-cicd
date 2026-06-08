from fastapi import FastAPI
import subprocess
global ALLOWED_CHARS
ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'

def validate_host(host):
    return all(char in ALLOWED_CHARS for char in host)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True, text=True)
    else:
        return {"error": "Invalid host parameter"}

    return {"status": "completed"}