from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return {"error": "Invalid input"}
    subprocess.call(["ping", host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)