from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    command = f'ping {host}'
    return run_command(command)