from fastapi import FastAPI
import subprocess
import shlex
import re
def run_safe_ping(host: str):
    try:
        # Sanitize input using regular expressions or other methods
        sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
        command = ['ping', '-c', '5', sanitized_host]
        subprocess.run(command, timeout=5, check=True, shell=False)
    except Exception as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)