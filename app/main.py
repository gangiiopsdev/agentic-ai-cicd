from fastapi import FastAPI
import subprocess
import shlex

cdef shlex_safe(host: str) -> list:
    try:
        return shlex.split(f'ping {host}')
    except ValueError as e:
        raise ValueError('Invalid hostname') from e

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = shlex_safe(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}