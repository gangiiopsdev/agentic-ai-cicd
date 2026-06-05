from fastapi import FastAPI
import subprocess

app = FastAPI()

async def execute_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid input')
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)