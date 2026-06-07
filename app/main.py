from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)

    return {"status": "completed", "output": result.stdout}