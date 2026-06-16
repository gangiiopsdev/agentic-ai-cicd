from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str):
    try:
        args = shlex.split(command)
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Command execution failed: {e}')

@app.get('/ping')
def ping(host: str):
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):  # Allow only local host
        command = f'ping {host}'
        execute_command(command)
    else:
        raise ValueError('Invalid host')  # Additional validation
    return {'status': 'completed'}