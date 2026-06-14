from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_string):
    return re.sub(r'[^a-zA-Z0-9-_.:/]', '', input_string)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    subprocess.call(shlex.split(f"ping {sanitized_host}"))
    return {"status": "completed"}