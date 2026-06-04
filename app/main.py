from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def execute_ping(host):
    try:
        # Sanitize the input to prevent command injection
        safe_host = subprocess.list2cmdline([host])
        output = await asyncio.create_subprocess_exec('ping', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = await output.communicate()
        if output.returncode == 0:
            return result[0].decode('utf-8').strip()
        else:
            return result[1].decode('utf-8').strip()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '.' in host or len(host) > 255:
        raise ValueError("Invalid host")
    result = await execute_ping(host)
    return {'status': 'completed', 'result': result}