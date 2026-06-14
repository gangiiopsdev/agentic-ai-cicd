from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

async def safe_ping(host: str):
    # Splitting host into separate arguments to prevent shell injection
    args = shlex.split(host)
    try:
        result = await global_app.state.executor.run(['ping'] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode('utf-8')}

@global_app.get("/ping")
def ping(host: str):
    return safe_ping(host)