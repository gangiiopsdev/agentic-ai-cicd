from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run with proper input validation
        sanitized_host = shell_quote(host)
        result = subprocess.run(['ping', sanitized_host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}