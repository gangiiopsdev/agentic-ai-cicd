from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host):
    try:
        # Use shlex.quote to safely escape the host parameter
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or len(host) > 255 or not host.replace('.', '', 1).isdigit():
        return {'status': 'error', 'message': 'Invalid host'}
    result = run_ping(host)
    return {'status': 'completed', 'output': result}