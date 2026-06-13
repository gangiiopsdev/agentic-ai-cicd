from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', '-c', '1', host, check=True, stdout=subprocess.PIPE)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': f'Ping failed: {e}'}, status_code=500)

@app.get("/ping")
async def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return JSONResponse(content={'error': 'Invalid input'}, status_code=400)
    return await safe_ping(host)