from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def execute_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    command = f'ping {shlex.quote(host)}'
    if not os.path.exists(host):  # Add validation to check if the host exists
        return {'status': 'error', 'message': 'Invalid host'}
    output, _ = execute_command(command)
    return {'status': 'completed', 'output': output.decode()}