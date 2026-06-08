from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = await output.communicate()
        if output.returncode == 0:
            return {'status': 'completed', 'output': result[0].decode()}
        else:
            return {'status': 'failed', 'error': result[1].decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}