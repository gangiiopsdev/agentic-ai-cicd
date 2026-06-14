from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    return await safe_ping(host)