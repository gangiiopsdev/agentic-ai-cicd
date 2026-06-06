from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_executable(executable):
    return executable.split()[0]

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(shlex.quote(host))
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}