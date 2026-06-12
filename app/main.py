from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid characters in host name')

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_host(host)
        # Safe implementation using subprocess.run with shell=False and argument unpacking
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}