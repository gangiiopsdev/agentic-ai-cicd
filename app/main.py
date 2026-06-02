from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping "{host}"')
    subprocess.run(args, check=True)
    return {'status': 'completed'}