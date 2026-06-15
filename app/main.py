from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

async def safe_ping(host: str):
    if host.strip() in ['127.0.0.1', 'localhost']:  # Example allowed hosts
        try:
            output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            if output.returncode != 0:
                return JSONResponse(status_code=500, content={'status': 'error', 'message': stderr.decode()})
            return JSONResponse(content={'status': 'completed', 'output': stdout.decode()})
        except Exception as e:
            return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})
    else:
        return JSONResponse(status_code=403, content={'status': 'not_allowed'})

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)