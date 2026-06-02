from fastapi import FastAPI
import subprocess
from shlex import quote
from os import path as ospath

app = FastAPI()

async def secure_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, output=stdout.decode(), stderr=stderr.decode())
        return stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)