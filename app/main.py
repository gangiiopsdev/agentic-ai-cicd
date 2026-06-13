from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid hostname")
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)
    return {"status": "completed"}