from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Dict

app = FastAPI()

cmd_options = {"ping": ["-c", "1"]}

@app.get('/ping')
def ping(host: str) -> Dict[str, str]:
    if host.strip().isalnum() and not '!' in host:
        sanitized_host = quote(host)
        result = subprocess.run(cmd_options[host], [sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid input'}