from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    try:
        command = ['ping', host]
        result = subprocess.run(command, check=True, timeout=5, capture_output=True)
        return result.stdout.decode('utf-8')
    except Exception as e:
        print(e)
        return False

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, bool):
        return {'status': 'completed', 'result': 'success' if result else 'failure'}
    else:
        return {'status': 'completed', 'result': result}