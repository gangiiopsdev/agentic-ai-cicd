from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    command_parts = ['ping', *shlex.split(host)]
    try:
        result = await asyncio.create_subprocess_exec(*command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        if isinstance(output, bytes):
            output = output.decode('utf-8')
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}