from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f'ping -c 1 {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}