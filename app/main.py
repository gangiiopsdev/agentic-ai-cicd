from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'stderr': e.stderr}, 400

def ping_endpoint(host: str):
    return ping(host)