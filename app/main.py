from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split('ping ' + host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}