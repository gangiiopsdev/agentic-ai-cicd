from fastapi import FastAPI
import subprocess

app = FastAPI()

async def execute_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            return f'Ping failed: {stderr.decode()}'
        return stdout.decode()
    except Exception as e:
        return f'An error occurred: {e}

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)