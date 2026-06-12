from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {'status': 'completed'}