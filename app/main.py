from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host parameter
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    return run_ping(host)