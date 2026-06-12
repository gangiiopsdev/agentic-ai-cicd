from fastapi import FastAPI
import subprocess
from shlex import quote
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(quote(c) for c in host if c.isalnum() or c in '.:-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(sanitized_host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}