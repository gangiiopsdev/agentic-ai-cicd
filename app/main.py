from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Add your validation logic here, e.g., allowed host patterns
    return True

class CommandSanitizer:
    @staticmethod
def sanitize_command(command):
        return [shlex.quote(arg) for arg in command]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = ['ping'] + CommandSanitizer.sanitize_command([host])
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}