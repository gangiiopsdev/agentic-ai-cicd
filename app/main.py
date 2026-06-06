from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        return subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}