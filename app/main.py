from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}