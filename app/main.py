from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Ensure host is sanitized to avoid command injection
    if not re.match(r'^[a-zA-Z0-9.-]{1,63}$', host) or '.' not in host:
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode == 0:
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': result.stderr}