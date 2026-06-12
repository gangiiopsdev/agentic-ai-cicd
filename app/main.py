from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)