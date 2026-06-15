from fastapi import FastAPI
import shlex
import subprocess

async def safe_subprocess(command):
    try:
        args = shlex.split(command)
        result = await asyncio.to_thread(subprocess.run, args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()