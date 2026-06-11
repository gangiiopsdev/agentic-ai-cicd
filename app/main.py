from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in host if char in allowed_chars)
    return sanitized

def execute_command(command, *args):
    try:
        output = subprocess.check_output([command] + list(args), stderr=subprocess.STDOUT, timeout=5, shell=False)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    success, output = execute_command('ping', '-c', '1', sanitized_host)
    if success:
        return JSONResponse({'status': 'completed', 'output': output})
    else:
        return JSONResponse({'status': 'failed', 'error': output}, status_code=400)