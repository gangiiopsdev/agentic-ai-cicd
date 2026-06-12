from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def run_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    ping_command = ['ping', shlex.quote(host)]
    try:
        result = await subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)