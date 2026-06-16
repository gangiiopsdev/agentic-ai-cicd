from fastapi import FastAPI
import subprocess
global_host = '127.0.0.1' # Replace with a fixed value or remove if not needed

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)