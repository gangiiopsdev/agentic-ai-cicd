from fastapi import FastAPI
import re
import subprocess

async def execute_ping(host):
    try:
        # Sanitize the host input using a whitelist approach
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-!@#$%^&*()_+[]{}|;:,.<>?'
        if not all(char in allowed_chars for char in host):
            raise ValueError('Invalid characters in host')
        result = await asyncio.create_subprocess_exec('ping', '-c', '4', host, capture_output=True, text=True)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=stderr)
        return {'status': 'completed', 'output': stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9._!]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)