from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    args = ['ping', host]
    try:
        await asyncio.create_subprocess_exec(*args)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    return {'status': 'completed'}