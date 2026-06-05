from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isnumeric() or len(host) > 3:
        raise ValueError('Invalid host format')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}