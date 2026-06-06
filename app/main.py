from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():
        return 'Invalid input'
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = await result.communicate()
    return output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}