from fastapi import FastAPI
import subprocess
import shlex
from typing import Union

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Basic validation: ensure host contains only alphanumeric characters and hyphens.
    return all(c.isalnum() or c == '-' for c in host)

@app.get("/ping")
def ping(host: Union[str, None] = None):  # Added type hint for better clarity
    if not host:
        raise ValueError('Host is required')
    if not is_valid_host(host):
        raise ValueError('Invalid host name')

    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)  # Added check=True to raise an exception on non-zero exit code
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}