from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(args):
    safe_args = [arg for arg in args if isinstance(arg, str) and all(c.isalnum() or c.isspace() for c in arg)]
    return safe_args

def validate_host(host):
    return host.strip().isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(safe_command(['ping'] + shlex.split(host)), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}