from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import Popen, PIPE, STDOUT

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        process = Popen(['ping', '-c', '1', quote(host)], stdout=PIPE, stderr=STDOUT, text=True)
        output, _ = process.communicate(timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}