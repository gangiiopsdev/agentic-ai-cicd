from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        raise ValueError("Invalid hostname")

    cmd = ["ping", *shlex.split(sanitized_host)]
    subprocess.run(cmd, check=True)

    return {"status": "completed"}