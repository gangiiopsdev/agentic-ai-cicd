from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

def ping(host: str):
    try:
        output = run_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}