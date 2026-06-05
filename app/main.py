from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode("utf-8")}'

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'error', 'result': 'Invalid characters in hostname'}
    result = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'result': result}