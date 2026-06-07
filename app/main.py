from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
        result = await asyncio.create_subprocess_exec(*args, check=True, capture_output=True, text=True)
        return True, result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
async def ping(host: str):
    success, output = await safe_ping(host)
    if not success:
        return {"status": "failed", "message": "Invalid host", "output": output}
    return {"status": "completed", "output": output}