from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize and quote the host to prevent shell injection
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}