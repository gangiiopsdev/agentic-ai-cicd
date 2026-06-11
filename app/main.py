from fastapi import FastAPI
import asyncio
from fastapi.responses import JSONResponse
def is_safe_hostname(hostname: str) -> bool:
    # Using a whitelist approach instead of regex for simplicity and security
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return all(char in allowed_chars for char in hostname)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host) or len(host) > 64:
        return JSONResponse({'status': 'failed', 'error': 'Invalid host name'}, status_code=400)

    async def ping_host(h: str) -> dict:
        try:
            result = await asyncio.create_subprocess_exec('ping', '-c', '1', h, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    return asyncio.run(ping_host(host))