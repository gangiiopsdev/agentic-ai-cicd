from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape host
        result = await asyncio.create_subprocess_exec('ping', shlex.quote(host), capture_output=True, text=True)
        output, _ = await result.communicate()
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}