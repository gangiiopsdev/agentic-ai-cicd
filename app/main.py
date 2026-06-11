from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host and all(char.isalnum() or char in ('.', '-') for char in host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}