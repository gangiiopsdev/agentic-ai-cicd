from fastapi import FastAPI
import subprocess
import shlex

async def safe_ping(host: str):
    try:
        # Use shlex to safely quote the host argument
        command = ['ping'] + shlex.split(host)
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return await safe_ping(host)