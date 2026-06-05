from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement your safe hostname validation logic here
    return hostname.isalnum()

def sanitize_command(command, *args):
    sanitized_args = [shlex.quote(arg) for arg in args]
    command_parts = shlex.split(command)
    full_command = command_parts + sanitized_args
    return ' '.join(full_command)

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        command = sanitize_command('ping', host)
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}