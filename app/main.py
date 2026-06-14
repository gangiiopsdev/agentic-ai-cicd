from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    try:
        args = ['ping', '-c', '1', host]
        output = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=5)
        return True, output.stdout.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    status, output = safe_ping(host)
    if status:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': output}