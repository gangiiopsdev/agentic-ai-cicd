from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Sanitize and escape the host parameter
    safe_host = shlex.quote(host)
    try:
        result = await asyncio.create_subprocess_exec('ping', safe_host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_safe(host: str):
    return ping(host)