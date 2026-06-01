from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not all(c.isalnum() or c in '.:-_' for c in host):
        return {'error': 'Invalid host'}, 400

    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

    return {'status': 'completed'}