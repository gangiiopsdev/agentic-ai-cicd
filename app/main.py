from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = await asyncio.create_subprocess_exec(*args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'stdout': (await result.stdout.read()).decode('utf-8'), 'stderr': (await result.stderr.read()).decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode('utf-8')}

app.add_api_route('/ping', ping, methods=['GET'])