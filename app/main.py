from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host: str):
    # Simple regex to allow only alphanumeric characters and periods
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

async def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        # Use shlex.quote to safely escape the host parameter
        safe_host = shlex.quote(host)
        result = await asyncio.create_subprocess_exec('ping', '-c 4', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=error)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)