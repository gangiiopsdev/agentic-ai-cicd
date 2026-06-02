from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        args = ['ping', '-c', '1', host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)