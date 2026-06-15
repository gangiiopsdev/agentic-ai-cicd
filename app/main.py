from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(cmd, args):
    try:
        output = subprocess.check_output(cmd + args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    cmd = ['ping']
    args = [shlex.quote(host)]  # Add shlex quoting to sanitize input
    return safe_subprocess(cmd, args)