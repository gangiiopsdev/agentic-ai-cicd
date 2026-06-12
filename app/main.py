from fastapi import FastAPI
import asyncio
import shlex
def escape_host(host: str):
    return shlex.quote(host)

app = FastAPI()

async def execute_ping(host: str):
    try:
        escaped_host = escape_host(host)
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', escaped_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return False
        return True
    except Exception as e:
        return False

@app.get("/ping")
def ping(host: str):
    return {"success": await execute_ping(shlex.quote(host))}