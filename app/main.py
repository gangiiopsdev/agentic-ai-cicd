from fastapi import FastAPI
import subprocess

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode().strip()}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    return await ping(host)