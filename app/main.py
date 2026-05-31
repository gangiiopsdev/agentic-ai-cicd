from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

async def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return JSONResponse(status_code=500, content={'error': error.decode('utf-8')})
        return {'output': output.decode('utf-8')}
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    response = safe_ping(host)
    return response