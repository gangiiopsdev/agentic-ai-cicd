from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail='Invalid host name')

    # Safe implementation
    subprocess.call(shlex.split(f'ping {host}'))

    return {'status': 'completed'}