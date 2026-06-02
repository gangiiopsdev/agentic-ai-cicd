from fastapi import FastAPI
import subprocess
import re
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid host'}

    # Sanitize the host input to prevent command injection
    sanitized_host = subprocess.quote(host)

    try:
        result = subprocess.run(['ping', '-c', '4', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}