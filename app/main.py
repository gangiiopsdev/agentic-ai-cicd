from fastapi import FastAPI
import subprocess
import asyncio
import shlex

app = FastAPI()

async def secure_ping(host: str):
    try:
        args = ['ping', host]
        output = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', output.stderr.decode())
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():  # Basic validation to prevent command injection
        raise ValueError('Invalid input')
    return secure_ping(shlex.quote(host))