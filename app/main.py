from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    result = await asyncio.create_subprocess_exec('ping', subprocess.list2cmdline([host]), stdout=subprocess.PIPE)
    output, _ = await result.communicate()
    return {'status': 'completed', 'output': output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)