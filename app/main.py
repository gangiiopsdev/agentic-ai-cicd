from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(lambda x: x in allowed_chars, user_input))

@app.get("/ping")
def ping(host: str):
    # Regular expression to allow only alphanumeric characters and specific symbols
    if re.match(r'^[a-zA-Z0-9.-_]+$', host):
        sanitized_host = sanitize_input(host)
        subprocess.call(shlex.split(f"ping {sanitized_host}"), shell=False)
        return {"status": "completed"}
    else:
        return {"status": "invalid input"}