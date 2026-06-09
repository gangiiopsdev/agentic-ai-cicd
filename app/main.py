from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_command(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = quote(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}