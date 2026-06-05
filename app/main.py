from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Sanitize and validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', f'/bin/ping'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'stderr': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return await safe_ping(host)