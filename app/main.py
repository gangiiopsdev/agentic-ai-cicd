from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in ['-', '.', '_', ':'] or char == '\')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    command = f'echo {shlex.quote(safe_host)}'
    result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'output': result.stdout.decode()}