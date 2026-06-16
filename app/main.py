from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run instead of subprocess.call with sanitized inputs
    subprocess.run(['ping', quote(host)], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}