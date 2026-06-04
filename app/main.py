from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError('Invalid host parameter')
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}