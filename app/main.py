from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', stderr=stderr)
        return JSONResponse(content={'status': 'completed', 'output': stdout.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': e.stderr.decode()}, status_code=e.returncode)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)