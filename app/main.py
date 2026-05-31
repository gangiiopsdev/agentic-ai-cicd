from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    return all(char in allowed_chars for char in hostname)

@app.get="/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError("Invalid input")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}