from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return 'Invalid host name'
    try:
        cmd = ['ping', shlex.quote(host)]
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode("utf-8")}'

@app.get('/ping')
def ping(host: str):
    return safe_ping(shlex.quote(host))