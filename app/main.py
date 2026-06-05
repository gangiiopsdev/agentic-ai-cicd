from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}