from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

async def run_ping(host):
    try:
        # Validate and sanitize host input to ensure it does not contain malicious content
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = await run_ping(host)
    return {'status': 'completed', 'response': response}