from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.run(['ping', quote(host)], check=True, capture_output=True)
    return {"status": "completed", "output": sanitized_host.stdout.decode('utf-8')}