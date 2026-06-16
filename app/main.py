from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it is safe to use with 'ping'
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def validate_host(host: str) -> bool:
    # Implement validation logic to ensure the host is safe for 'ping'
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None