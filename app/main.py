from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if any(char in host for char in [';', '&', '|', '*', '?', '<', '>']):
        return {"error": "Invalid input detected"}
    args = ['ping', quote(host)]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}