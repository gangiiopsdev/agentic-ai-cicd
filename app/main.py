from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Sanitize input to prevent command injection
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Escape command arguments properly
    escaped_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'result': result.stdout}