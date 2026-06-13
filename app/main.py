from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def execute_safe_command(command, *args):
    try:
        args = [shlex.quote(arg) for arg in args]
        result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

def ping(host: str):
    if host.isalnum():
        output = await execute_safe_command('ping', host)
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': 'Invalid input'}