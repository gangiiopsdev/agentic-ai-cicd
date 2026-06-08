from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')

    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}