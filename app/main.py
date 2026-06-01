from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.call(args)
    return result == 0

@app.get("/ping")
def ping(host: str):\n    if safe_ping(host):\n        return {"status": "completed", "message": "Ping successful"}\n    else:\n        return {"status": "failed", "message": "Ping failed"}