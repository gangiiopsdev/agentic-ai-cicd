from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Validate the host to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host): raise ValueError('Invalid host')
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True, timeout=10)
        return {'status': 'completed', 'output': (await result.stdout.read()).decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return asyncio.run(ping(host))