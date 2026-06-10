from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def safe_ping(host):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in '-.:/')
    args = ['ping', *shlex.split(safe_host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    response = safe_ping(shlex.quote(host))  # Use shlex.quote to escape special characters
    return {'status': 'completed', 'response': response}