from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isdigit():
        raise ValueError("Invalid host")
    return subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}