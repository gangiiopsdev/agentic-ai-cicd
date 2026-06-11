from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if 'ping' in host or '||' in host or ';' in host:
        raise ValueError('Invalid host input')
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}