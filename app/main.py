from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use shlex to safely quote the host input
        command = ['ping', shlex.quote(host)]
        result = await asyncio.create_subprocess_exec(*command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)