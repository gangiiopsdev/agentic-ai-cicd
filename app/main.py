from fastapi import FastAPI
import subprocess
cimport shlex

c = shlex

app = FastAPI()

@app.get('/ping_secure')
def ping_secure(host: str):
    if not host.replace('.', '').replace('-', '').isalnum():  # Improved validation
        return {'status': 'error', 'message': 'Invalid input'}
    args = c.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}

# Additional preventive controls:
# 1. Use a whitelist for allowed hosts.
# 2. Validate the length of the host parameter to prevent excessively long strings.
# 3. Log all input parameters for auditing purposes.