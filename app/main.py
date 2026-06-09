from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', f'"{host}"'], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return {'status': safe_ping(host)}
    else:
        return {'error': 'Invalid host'}