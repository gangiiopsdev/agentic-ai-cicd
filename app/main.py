from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'error', 'output': 'Invalid hostname'}
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}