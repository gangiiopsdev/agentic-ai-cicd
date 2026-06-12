from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = shlex.split(f'ping {shlex.quote(host)}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)

# Preventive controls:
# 1. Validate and sanitize user inputs.
# 2. Use parameterized commands instead of shell=True.
# 3. Limit the scope of privileges used by the application.