from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = shlex.split('ping ' + host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}