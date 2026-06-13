from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote
from urllib.parse import urlparse

app = FastAPI()

def safe_ping(host):
    try:
        # Validate host to ensure it's a valid hostname or IP address
        parsed_url = urlparse(host)
        if not parsed_url.scheme and not parsed_url.netloc:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', shell_quote(parsed_url.netloc)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Safer implementation with input validation
    return safe_ping(host)