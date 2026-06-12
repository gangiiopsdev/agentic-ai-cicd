from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command_parts):
    subprocess.run(command_parts, check=True)

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_subprocess_call(['ping', shlex.quote(host)])
    return {'status': 'completed'}