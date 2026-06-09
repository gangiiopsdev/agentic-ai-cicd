from fastapi import FastAPI
import subprocess
getent = __import__('getent')

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', '-c', '1', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': (await output.stdout.read()).decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': (await e.stderr.read()).decode()}

@app.get("/ping")
def ping_route(host: str):
    try:
        getent.hosts(host)
    except KeyError:
        return {'status': 'failed', 'error': 'Invalid input'}
    return await ping(host)