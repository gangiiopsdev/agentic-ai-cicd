from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result, _ = await output.communicate(timeout=5)
        return {'status': 'completed', 'output': result.decode()}
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
async def ping(host: str):
    return await safe_ping(host)