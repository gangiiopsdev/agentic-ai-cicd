from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with basic input validation
    if not host.isdigit():
        return {"status": "Invalid input"}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}