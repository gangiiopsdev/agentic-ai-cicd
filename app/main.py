from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

async def ping(host: str):
    # Safe implementation using list of arguments
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if error:
            return JSONResponse(content={'error': error.decode()}, status_code=500)
        else:
            return JSONResponse(content={'output': output.decode()})
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)

@app.get("/ping")
async def ping_route(host: str):
    return await ping(host)