from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not any(char in host for char in [';', '&', '|', '>', '<', '*', '?', '$', '`']):
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}