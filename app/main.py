from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command, *args):
    try:
        result = subprocess.run([command] + [shlex.quote(arg) for arg in args], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    output = safe_subprocess('ping', '-c', '1', host)
    return {'status': 'completed', 'output': output}