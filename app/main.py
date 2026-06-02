from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping_safe(host: str):
    try:
        # Use safe method to avoid shell injection
        await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = ping_safe(host)
    return result