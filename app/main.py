from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

async def ping(host: str):
    try:
        if not host or ' ' in host:
            raise ValueError('Invalid hostname')
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}