from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ["ping", "-c", "1", host]  # Use the ping command with specific options to avoid injection
        process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        return await safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}