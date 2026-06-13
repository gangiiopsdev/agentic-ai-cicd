from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return run_ping(host)

def validate_host(host):
    # Add validation logic here to ensure the host is safe to use with subprocess
    import re
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return bool(re.match(pattern, host))