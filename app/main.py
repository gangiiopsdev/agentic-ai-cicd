from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it contains only allowed characters (e.g., alphanumeric and some punctuation)
    if not re.match(r'^[a-zA-Z0-9_.-]+$', host):
        return {'status': 'error', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

# Preventive controls:
# - Use a whitelist for allowed hosts instead of regex validation.
# - Implement rate limiting to prevent abuse.
# - Log and monitor all ping requests for anomalous activity.