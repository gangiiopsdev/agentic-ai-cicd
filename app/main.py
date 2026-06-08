from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host and isinstance(host, str) and 'ping' not in host:
        args = ['ping', host]
        subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}