from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Regex to validate hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    command = shlex.split(f"ping {host}")
    subprocess.run(command, check=True)
    return {"status": "completed"}