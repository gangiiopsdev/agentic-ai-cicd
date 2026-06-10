from fastapi import FastAPI, HTTPException
import subprocess
gimport shlex

app = FastAPI()

async def safe_ping(host):
    if not host.strip():
        raise HTTPException(status_code=400, detail='Invalid host')
    try:
        safe_host = shlex.quote(host)
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f'Error: {error.decode()}')
        return output.decode()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {'status': 'completed', 'output': output}