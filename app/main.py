from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(c in allowed_chars for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return output.decode('utf-8').strip()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}