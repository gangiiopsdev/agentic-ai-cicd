from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_wrapper(host: str):
    if not host or len(host) > 255 or not all(c.isalnum() for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)