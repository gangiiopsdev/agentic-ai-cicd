from fastapi import FastAPI
import subprocess
import shlex
global_app = FastAPI()

def ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e), 'stdout': e.output}