from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command: str):
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    command = f'ping {host}'
    try:
        output = run_command(command)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}