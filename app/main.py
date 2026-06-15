from fastapi import FastAPI
import subprocess
import shlex
import shlex

app = FastAPI()

def sanitize_host(host):
    return shlex.quote(host)

def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command_parts = ['ping', sanitized_host]
    return run_safe_command(command_parts)