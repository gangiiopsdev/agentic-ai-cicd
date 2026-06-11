from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_execute_command(command: str, args: list):
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    args = ['ping', quote(host)]
    return safe_execute_command('Ping command failed', args)