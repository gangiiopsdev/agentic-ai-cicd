from fastapi import FastAPI
import subprocess
import shlex
def escape_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in '.-_')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = escape_input(host)
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}