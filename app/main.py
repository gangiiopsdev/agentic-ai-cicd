from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in hostname)

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}