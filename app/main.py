from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

def run_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return True, output.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

def ping(host: str):
    sanitized_host = sanitize_input(host)
    success, result = run_ping(sanitized_host)
    if success:
        return {'status': 'completed', 'output': result}
    else:
        return {'status': 'failed', 'error': result}