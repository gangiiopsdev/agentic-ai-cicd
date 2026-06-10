from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if any(char in host for char in [';', '&', '|', '*', '?', '<', '>']):
        return {"error": "Invalid input detected"}
    args = ['ping', quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}