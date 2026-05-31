from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command):
    return [part for part in shlex.split(command)]

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(safe_command(f'ping {host}'), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}