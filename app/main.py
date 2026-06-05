from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', escape_shell_arg(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}