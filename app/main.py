from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host):
    # More comprehensive regex to validate the host input
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

def shell_safe_command(command, args):
    safe_args = [shlex.quote(arg) for arg in args]
    return command + ' ' + ' '.join(safe_args)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Validate the host input using a more comprehensive regex
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run([shell_safe_command('ping', [host])], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}