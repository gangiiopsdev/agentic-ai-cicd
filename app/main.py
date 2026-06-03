from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'stdout': output.decode(), 'stderr': error.decode()}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)