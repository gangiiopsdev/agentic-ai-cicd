from fastapi import FastAPI
import subprocess
global_env = os.environ.copy()
global_env['PATH'] = "/usr/sbin:/sbin:/usr/bin:/bin"  # Set PATH to prevent directory traversal

app = FastAPI()

def ping_safe(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, env=global_env)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Add input validation to restrict the characters allowed in the host parameter
        return {'status': 'failed', 'error': 'Invalid host parameter'}
    return ping_safe(host)