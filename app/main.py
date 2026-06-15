from fastapi import FastAPI
import subprocess
import shlex
import os

global_config = {
    'ping': '/bin/ping',
}

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    full_command = [global_config['ping'], sanitize_input(host)]
    subprocess.run(full_command, check=True, shell=False)
    return {'status': 'completed'}