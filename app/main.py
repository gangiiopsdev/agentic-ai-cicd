from fastapi import FastAPI
import subprocess
import re

allowed_hosts = ['example.com', 'test.com']  # Replace with actual whitelist logic

async def safe_ping(host: str):
    if host not in allowed_hosts:
        return "Invalid input"
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', re.escape(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, output=stdout.decode(), stderr=stderr.decode())
        return stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return "Invalid input"
    return await safe_ping(host)