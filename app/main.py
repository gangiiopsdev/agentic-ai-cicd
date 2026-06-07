from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum() or '..' in host:
        return JSONResponse(status_code=400, content={'status': 'failed', 'error': 'Invalid host input'})
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={'status': 'failed', 'error': str(e)})

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return await safe_ping(host)