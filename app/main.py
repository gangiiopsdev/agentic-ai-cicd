from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Secure implementation using shlex.quote to escape any special characters in host
        import shlex
        escaped_host = shlex.quote(host)
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}