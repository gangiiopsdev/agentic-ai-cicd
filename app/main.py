from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host):
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(shlex.split(f"ping {host}"), check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}