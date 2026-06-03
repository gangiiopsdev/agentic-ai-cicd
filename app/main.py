from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the input more strictly
        if host not in ['example.com', 'test.com'] or not all(c.isalnum() for c in host):
            raise ValueError('Invalid host')
        args = shlex.split(f'ping -c 4 {shlex.quote(host)}')  # Sanitize input and use ping with count for security
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum() or host in ['example.com', 'test.com']:
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)