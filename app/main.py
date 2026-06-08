from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'Success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'Failure', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in ("-", ".") for c in host):
        return {'status': 'Failure', 'error': 'Invalid host'}
    return ping(host)