from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def run_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        error = await result.stderr.read()
        return {'status': 'failed', 'error': error.decode('utf-8')}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_ping(shlex.quote(host))