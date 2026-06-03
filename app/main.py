from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use subprocess.run for a safer approach with proper quoting of the host parameter
cmd = ['ping', quote(host)]
result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Add input validation
        return {'status': 'invalid', 'message': 'Invalid input'}
    return await safe_ping(host)