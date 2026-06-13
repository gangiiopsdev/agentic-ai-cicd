from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Unauthorized access attempt')
    try:
        output = await asyncio.create_subprocess_exec('ping', subprocess.list2cmdline([host]), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode().strip()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Unauthorized access attempt')
    return ping(host)