from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    # Use subprocess.Popen instead of subprocess.run for better control and security
    args = shlex.split(f'ping {host}')
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed: {error.decode()}')
    return {'status': 'completed', 'output': output.decode()}

# Preventive controls
1. Always validate and sanitize user input before using it in subprocess calls.
2. Avoid using shell=True if not absolutely necessary, as it can lead to command injection vulnerabilities.
3. Consider using higher-level libraries like `ping3` for safer network operations.