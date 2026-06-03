from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_ping(host):
    cmd = shlex.split(f'ping {host}')
    try:
        process = await asyncio.create_subprocess_exec(*cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = await process.communicate()
        return {'status': 'success', 'output': result[0].decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)