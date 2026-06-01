from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host input"}
    try:
        # Use shlex to safely handle the host input
        args = ['ping'] + shlex.split(host)
        subprocess.call(args, shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}