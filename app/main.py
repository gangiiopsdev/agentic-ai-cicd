from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.subprocess.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = await output.wait()
        return output.stdout.decode('utf-8')
    except (subprocess.CalledProcessError, TimeoutExpired) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}