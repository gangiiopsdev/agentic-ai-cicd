from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Use shlex.quote to ensure the host is properly quoted
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}

@app.get("/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:  # Restrict allowed hosts for security
        return {'status': 'error', 'output': 'Unauthorized host'}
    return safe_ping(host)