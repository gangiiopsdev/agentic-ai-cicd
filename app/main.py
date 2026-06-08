from fastapi import FastAPI
import subprocess
import shlex
def run_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, timeout=5, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    return run_command(command_parts)