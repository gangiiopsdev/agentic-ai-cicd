from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_argument(arg):
    return ' '.join(shlex.quote(c) for c in arg.split())
global_app = FastAPI()
@globa_app.get('/ping')
def ping(host: str):
    escaped_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}