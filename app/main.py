from fastapi import FastAPI
import subprocess
import re
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid host name'}
    try:
        # Sanitize the input by escaping shell metacharacters
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}