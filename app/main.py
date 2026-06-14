from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host: str) -> bool:
    return all(char not in host for char in [';', '|', '&', '`'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid input'}, 400
    command = ['ping', *shlex.split(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}