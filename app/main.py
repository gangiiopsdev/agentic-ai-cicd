from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        cmd = ['ping', host]
        result = await asyncio.to_thread(subprocess.run, cmd, check=True, timeout=5, capture_output=True)
        return {'status': 'success', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)