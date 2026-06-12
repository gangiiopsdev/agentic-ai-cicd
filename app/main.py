from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    args = shlex.split('ping ' + host)
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}

@app.get('/ping')
async def ping_wrapper(host: str):
    return await ping(host)