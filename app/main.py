from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

async def execute_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        raise Exception(f'Error executing ping command: {error.decode()}')
    return output.decode()

@global_app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {"status": "completed", "output": output}