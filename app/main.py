from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        # Use shlex.quote to safely handle user inputs
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}