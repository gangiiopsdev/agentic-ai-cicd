from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to avoid injection attacks
    sanitized_host = escape_host(host)
    try:
        result = subprocess.run(shlex.split('ping {}'.format(sanitized_host)), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}