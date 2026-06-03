from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not all(c.isalnum() or c in '.,-: ' for c in host):
        raise ValueError("Invalid characters in host")
    return subprocess.call(['ping', shlex.quote(host)])

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400