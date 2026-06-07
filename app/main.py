from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_ping(host: str):
    try:
        # Constructing the ping command safely using subprocess.run
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)