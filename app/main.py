from fastapi import FastAPI
import subprocess
import re
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', f'-c 1 {shlex.quote(host)}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}