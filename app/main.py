from fastapi import FastAPI
import subprocess
global_subprocess_lock = asyncio.Lock()

app = FastAPI()

async def ping(host: str):
    async with global_subprocess_lock:
        try:
            output = await asyncio.to_thread(subprocess.check_output, ['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)