from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    # Ensure the host is safe to use in ping command
    if '/' in host or ' ' in host:
        raise ValueError('Invalid host input')
    args = ['ping'] + [arg for arg in shlex.split(host) if not any(c in arg for c in ('&', '|', ';'))]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return {'output': output.decode(), 'error': error.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)