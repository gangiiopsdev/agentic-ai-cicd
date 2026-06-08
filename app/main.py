from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host parameter
        output = await asyncio.create_subprocess_exec('ping', shlex.quote(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = await output.communicate()
        return result[0].decode('utf-8')
    except Exception as e:
        return str(e)

@app.get('/ping/{host}')
async def ping(host: str):
    result = await safe_ping(host)
    return {'status': 'completed', 'result': result}