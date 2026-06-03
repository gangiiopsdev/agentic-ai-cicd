from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_host = subprocess.list2cmdline([host])
    try:
        result = subprocess.run(['ping', '--'], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}