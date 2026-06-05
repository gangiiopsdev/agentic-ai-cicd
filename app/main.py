from fastapi import FastAPI
import subprocess
import shlex

async def safe_ping(host):
    try:
        args = ['ping'] + shlex.split(host)
        result = await asyncio.to_thread(subprocess.run, args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = await safe_ping(host)
    if 'error' in result:
        return result
    else:
        return result