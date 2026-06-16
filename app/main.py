from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def run_ping(host: str):
    # Validate the host parameter to prevent command injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    try:
        # Use a full path to avoid execution with a partial path
        result = await asyncio.create_subprocess_exec('/usr/bin/ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=error)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode().strip()}'

def is_valid_host(host: str) -> bool:
    # Simple validation example
    if re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.\d{1,3}$', host):
        parts = host.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {'status': 'completed', 'output': output}