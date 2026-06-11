from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.subprocess.create_subprocess_exec('ping', host, stderr=asyncio.subprocess.PIPE, timeout=5)
        result = await output.wait()
        if result.returncode == 0:
            return {'status': 'completed', 'output': (await output.stdout.read()).decode()}
        else:
            return {'status': 'failed', 'error': (await output.stderr.read()).decode()}
    except asyncio.TimeoutError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return await ping(host)