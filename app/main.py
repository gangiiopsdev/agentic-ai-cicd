from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Host parameter is required')
    # Sanitize input to prevent command injection
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

    return {'status': 'completed'}