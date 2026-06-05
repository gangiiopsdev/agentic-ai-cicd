from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command):
    return subprocess.run(command, capture_output=True, text=True, timeout=5)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        command = ['ping', safe_host]
        result = safe_subprocess(command)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}