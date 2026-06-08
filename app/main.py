from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # More restrictive validation: allow only alphanumeric and some special characters, no shell metacharacters or command separators
    return re.match(r'^[a-zA-Z0-9.-_]+$', host) is not None

def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}