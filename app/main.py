from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Further validate host to ensure it does not contain harmful characters
    if not host or not all(c.isalnum() for c in host) or not all(c in string.printable for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}