from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)