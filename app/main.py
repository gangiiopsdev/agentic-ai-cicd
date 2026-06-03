from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Sanitize the input to avoid command injection
    if not host.strip().isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Sanitize the input to avoid command injection
    if not host.strip().isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    return await ping(host)