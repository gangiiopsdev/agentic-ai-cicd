from fastapi import FastAPI
import subprocess

app = FastAPI()

async def execute_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        error = await result.stderr.read()
        return {'status': 'failed', 'error': error.decode()}

@app.get("/ping")
async def ping(host: str):
    return await execute_ping(host)