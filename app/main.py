from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    # Safe implementation using shlex.quote to escape arguments
    args = ['ping', shlex.quote(host)]
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True)
        return result
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}