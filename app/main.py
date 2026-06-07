from fastapi import FastAPI
import subprocess
import shlex

global_config = {
    'allowed_hosts': ['127.0.0.1', '::1']
}

app = FastAPI()

async def run_ping(host):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        await run_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}