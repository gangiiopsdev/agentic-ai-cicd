from fastapi import FastAPI
import shlex
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Using shlex.quote to safely escape command arguments
    quoted_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', quoted_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

def validate_input(host):
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return False
    return True

@app.get('/ping')
def ping(host: str):