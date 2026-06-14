from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse
def escape_command(cmd):
    return [arg.replace(';', '').replace('&', '') for arg in cmd]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    try:
        parsed_url = urlparse(host)
        if not parsed_url.hostname:
            raise ValueError('Invalid hostname')
        output = subprocess.run(escape_command(['ping', parsed_url.hostname]), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}