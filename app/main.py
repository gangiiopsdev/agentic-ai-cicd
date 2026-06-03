from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "error": "Invalid host input"}
    try:
        output = subprocess.check_output([quote('ping'), quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e.output)}