from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)