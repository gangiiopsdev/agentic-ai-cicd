from fastapi import FastAPI
import subprocess
import re
import shlex
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if re.match(r'^[a-zA-Z0-9]+$', host) is None:
        return '', 'Invalid input'
    sanitized_host = shlex.quote(host)
    args = ['ping', '-c', '1', sanitized_host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return '', f'Error: {e}

def validate_ping_output(output: str) -> bool:
    # Add validation logic to ensure the output is safe
    return 'Invalid output' not in output  # Adjust the regex or string check as needed

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    if validate_ping_output(output):
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'message': 'Invalid output'}