from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not host or len(host) > 255:
        return {"error": "Invalid host input"}, 400
    command = ["ping", shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}