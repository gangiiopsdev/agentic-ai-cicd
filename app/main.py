from fastapi import FastAPI
import subprocess
import shlex
import re

def sanitize_input(user_input):
    # Add your sanitization logic here
    return re.sub(r'[^a-zA-Z0-9.-]', '', user_input)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.call(shlex.split(f'ping -c 1 {shlex.quote(sanitized_host)}'))
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}