from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command, args):
    full_command = [command] + list(map(shlex.quote, args))
    result = subprocess.run(full_command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        return safe_subprocess('ping', ['-c', '1', host])
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}