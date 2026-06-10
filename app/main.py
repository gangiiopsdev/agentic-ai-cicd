from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = subprocess.call(["ping", host])
    if result == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping command failed"}