from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def secure_ping(host):
    # Secure implementation using shlex.quote to escape special characters
    return ['ping', '-c', '1', quote(host)]

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(secure_ping(host), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}