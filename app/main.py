from fastapi import FastAPI
import subprocess
import re
import shlex
def safe_ping(host: str) -> str:
    try:
        # Validate and sanitize host input
        if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
            raise ValueError("Invalid host")
        args = ['ping', '-c', '1', host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e).decode('utf-8')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}