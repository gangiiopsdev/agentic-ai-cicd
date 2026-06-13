from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', stderr=stderr)
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}