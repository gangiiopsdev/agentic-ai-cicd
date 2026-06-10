from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}