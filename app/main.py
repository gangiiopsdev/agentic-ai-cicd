from fastapi import FastAPI
import asyncio
import shlex
def safe_ping(host: str):
    try:
        # Validate the host to prevent command injection
        if not host.isalnum() and not '.' in host and not host.startswith('-') and not host.endswith('-') and '--' not in host:
            raise ValueError('Invalid host')
        # Constructing the ping command safely using subprocess.run
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)