from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using shlex.quote to sanitize input
    subprocess.call(['ping', quote(host)], shell=False, cwd=None)

@app.get("/ping")
def ping(host: str):
    try:
        if os.name == 'nt':  # Windows
            run_ping(f'\\\{host}')
        else:
            run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}