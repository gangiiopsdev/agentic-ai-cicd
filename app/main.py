from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'status': 'completed' if result.returncode == 0 else 'error', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.stderr.decode())}