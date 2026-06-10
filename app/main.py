from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Add robust validation logic here, e.g., checking against a whitelist of allowed hosts
    return host in ['127.0.0.1', '::1']  # Example whitelist

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Additional preventive controls:
# 1. Use a more robust validation function that includes regular expressions or other checks.
# 2. Consider using parameterized queries if the host input is part of a larger query.
# 3. Limit the permissions of the process running this code to minimize potential damage if exploited.