from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise ValueError(error)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
async def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Sanitize the host parameter
    safe_host = shlex.quote(host)
    return await safe_ping(safe_host)