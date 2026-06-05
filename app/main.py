from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum():
        raise ValueError('Invalid host')
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return output.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}