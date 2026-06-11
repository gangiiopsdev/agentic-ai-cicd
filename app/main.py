from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        args = shlex.split('ping ' + host)
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True, check=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)