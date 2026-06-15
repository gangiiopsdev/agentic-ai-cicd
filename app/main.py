from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def execute_ping(host: str):
    try:
        command = ['ping', host]
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode(), stderr.decode()
    except Exception as e:
        return str(e), None

def ping(host: str):
    output, error = execute_ping(host)
    if error:
        return {'status': 'failed', 'error': error}
    else:
        return {'status': 'completed', 'output': output}