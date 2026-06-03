from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex pattern matching)
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None