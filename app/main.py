from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Sanitize the host input to prevent command injection
    try:
        args = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(host)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}