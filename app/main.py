from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_ping(host: str):
    # Splitting the host to avoid shell injection
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

def ping(host: str):
    is_safe, output = safe_ping(host)
    if is_safe:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': output}