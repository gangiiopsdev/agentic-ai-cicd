from fastapi import FastAPI
import subprocess
import shlex
def safe_command(command: str) -> list:
    return shlex.split(command)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}