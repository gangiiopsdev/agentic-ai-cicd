from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def escape_shell_command(input_string):
    return ' '.join(shlex.quote(arg) for arg in input_string.split())

@app.get('/ping')
def ping(host: str):
    safe_host = await escape_shell_command(host.strip())
    if not safe_host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        subprocess.run(['ping', *safe_host.split()], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}