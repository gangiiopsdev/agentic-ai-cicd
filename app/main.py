from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if host.strip() and '@' not in host:
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)
    else:
        raise ValueError('Invalid hostname provided')
    return {'status': 'completed'}

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return response
    except ValueError as e:
        return {'error': str(e)}, 400