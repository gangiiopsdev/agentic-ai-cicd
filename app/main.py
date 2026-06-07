from fastapi import FastAPI
import subprocess
import shlex
import re

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
    if sanitized_host and len(sanitized_host) <= 255:
        subprocess.call(shlex.split(f"ping {sanitized_host}"), shell=False)
    return {"status": "completed"}