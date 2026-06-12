from fastapi import FastAPI
import subprocess
import shlex
import re

global app = FastAPI()

def sanitize_input(user_input):
    return re.sub(r'[^a-zA-Z0-9.-_]', '', user_input)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = shlex.split(f"ping {sanitized_host}")
    subprocess.run(command, check=True)
    return {"status": "completed"}