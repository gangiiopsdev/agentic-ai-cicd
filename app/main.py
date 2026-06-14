from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(user_input):
    return re.sub(r'^[a-zA-Z0-9.-_]*$', '', user_input)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not re.match('^[a-zA-Z0-9.-_]*$', sanitized_host):
        raise ValueError('Invalid input')
    command = shlex.split(f"ping {sanitized_host}")
    subprocess.run(command, check=True, capture_output=True, text=True, input=None)
    return {"status": "completed", "output": result.stdout}