from fastapi import FastAPI
import subprocess
import shlex
import re
globally_allowed_hosts = ['example.com', 'test.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in globally_allowed_hosts:
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(shlex.quote(host))
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}