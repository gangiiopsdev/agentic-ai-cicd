from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if re.match(r'^[a-zA-Z0-9]+$', host) is None:
        return '', 'Invalid input'
    sanitized_host = shlex.quote(host)
    args = ['ping', sanitized_host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return '', f'Error: {e}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    return {'status': 'completed', 'output': output}