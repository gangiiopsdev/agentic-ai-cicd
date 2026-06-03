from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host:
        return {'error': 'Host is required'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        output = await result.communicate()
        return {'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)