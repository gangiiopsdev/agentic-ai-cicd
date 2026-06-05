from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)