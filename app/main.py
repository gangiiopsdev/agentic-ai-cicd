from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid host input'}
    args = shlex.split('ping {}'.format(host))
    subprocess.run(args, check=True)
    return {'status': 'completed'}