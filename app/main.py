from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Validate input to ensure it only contains allowed characters and does not contain shell metacharacters
    if not host.isalnum() or any(char in host for char in set('`$\";<>|&*?{}[]()+=~!@#%^&*')):
        raise ValueError('Invalid input for ping command')

    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
async def ping(host: str):
    return await safe_ping(host)