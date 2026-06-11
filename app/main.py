from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.call(['ping', '-c', '1', host]) == 0
    else:
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "error", "message": "Invalid host for ping"}