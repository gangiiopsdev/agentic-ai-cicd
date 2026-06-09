from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_command(command_parts):
    try:
        output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(host)
    command_parts = ['ping', '-c', '1', sanitized_host]
    return run_command(command_parts)