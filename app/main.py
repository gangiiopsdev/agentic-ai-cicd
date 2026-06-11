from fastapi import FastAPI
import subprocess
import shlex
from typing import Union

app = FastAPI()

@app.get('/ping')
def ping(host: str) -> Union[dict, tuple]:
    # Validate and sanitize input
    if not host or len(host) > 100:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split('ping ' + shlex.quote(host))
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}