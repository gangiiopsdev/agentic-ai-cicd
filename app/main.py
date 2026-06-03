from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Basic validation: ensure host contains only alphanumeric characters and hyphens.
    return host.replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host name')

    # Secure implementation using subprocess.run to safely execute the command
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}