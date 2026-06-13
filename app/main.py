from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate the host input
        if not all(c in string.ascii_letters + string.digits for c in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        
        # Use a safe method to construct the command
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, timeout=10)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)