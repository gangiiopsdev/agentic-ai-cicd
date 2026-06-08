from fastapi import FastAPI
import subprocess
from subprocess import TimeoutExpired

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host or not isinstance(host, str) or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except TimeoutExpired:
        return {'status': 'timeout', 'message': 'Operation timed out'}

# Additional recommendation: Use a whitelist for allowed hosts instead of sanitizing input.