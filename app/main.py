from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    subprocess.run(['ping', sanitized_host], check=True, text=True)
    return {"status": "completed"}