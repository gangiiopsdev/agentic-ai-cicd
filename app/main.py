from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result, error = await output.communicate()
        if output.returncode != 0:
            return {'status': 'failed', 'error': error.decode('utf-8')}
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)