from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def safe_ping(host):
    # Validate the input to ensure it does not contain harmful characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Escape the user input to prevent command injection
    escaped_host = re.escape(host)
    return safe_ping(escaped_host)