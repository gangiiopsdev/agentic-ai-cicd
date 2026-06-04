from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}