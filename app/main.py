from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex to safely handle command arguments
    allowed_hosts = ['localhost', '127.0.0.1']  # Add allowed hosts here
    if host in allowed_hosts:
        try:
            args = shlex.split(f'ping {shlex.quote(host)}')
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e), 'stderr': e.stderr}
    else:
        return {'status': 'error', 'message': 'Invalid host'}