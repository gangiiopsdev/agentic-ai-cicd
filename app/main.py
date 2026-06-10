from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    return host.replace(';', '').replace('&', '')

app = FastAPI()

async def execute_ping(host: str):
    try:
        escaped_host = escape_host(host)
        result = await asyncio.create_subprocess_exec('ping', escaped_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return False
        return True
    except Exception as e:
        return False

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}
    return {'success': await execute_ping(host)}