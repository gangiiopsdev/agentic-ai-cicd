from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation and sanitization
    if not host.isnumeric() or len(host) > 3:
        raise ValueError('Invalid hostname provided')
    args = ["ping", host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}