from fastapi import FastAPI
import os
import shlex
global_loop = asyncio.get_running_loop()

app = FastAPI()

def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        args = ['ping', '-c', '1', safe_host]
        process = global_loop.run_in_executor(None, subprocess.Popen, args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = await process.communicate()
        return {'status': 'completed', 'output': result[0]}
    except (subprocess.CalledProcessError, Exception) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping/{host}")
def read_ping(host: str):
    return ping(host)