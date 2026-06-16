from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if host.isalnum() and '-' in host:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400