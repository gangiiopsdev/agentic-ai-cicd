from fastapi import FastAPI
import shlex
import subprocess

def ping(host: str):
    try:
        # Validate and sanitize input further before passing to the subprocess
        if not host or len(host) > 255 or not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError('Invalid host')
        # Sanitize input to avoid command injection
        sanitized_host = shlex.quote(host)
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize input further before passing to the subprocess
    if not host or len(host) > 255 or not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)