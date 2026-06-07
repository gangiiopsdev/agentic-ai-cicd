from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple check to ensure host does not contain potentially harmful characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(f"ping {host}", shell=True)
    else:
        return {"error": "Invalid host parameter"}

    return {"status": "completed"}