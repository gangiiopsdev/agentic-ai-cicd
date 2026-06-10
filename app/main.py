from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(shlex.split(f"ping {host}"))
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}