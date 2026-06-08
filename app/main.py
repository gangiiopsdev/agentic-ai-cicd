from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation without shell=True
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)