from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)