from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': await safe_ping(host)}