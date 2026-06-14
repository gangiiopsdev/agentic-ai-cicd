from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Host parameter is empty or contains only whitespace. Please provide a valid hostname.')
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}