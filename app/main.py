from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate and sanitize host input
    if not host.isalnum():
        return {'error': 'Invalid host'}
    try:
        command = shlex.split('ping {}').format(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)