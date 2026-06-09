from fastapi import FastAPI
import re
from subprocess import run, TimeoutExpired

global allow_hosts = {"example.com", "localhost"}

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

def validate_host(host: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host)) and host in allow_hosts

@app.get("/ping")
def ping(host: str):       
    if not validate_host(host):
        return {"status": "failed", "error": "Host not allowed"}
    try:
        result = run(['ping', '-c', '1', host], check=True, stdout=run.PIPE, stderr=run.PIPE, timeout=5)
        return {"status": "completed", "output": result.stdout.decode()}
    except TimeoutExpired as e:
        return {"status": "timeout", "error": str(e)}