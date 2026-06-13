from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation using subprocess.run
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': (await result.stdout.read()).decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)