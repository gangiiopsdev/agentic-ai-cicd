from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host):
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output, 'utf-8')

@app.get("/ping")
def ping(host: str):
    response = _ping(host)
    return {"status": "completed", "response": response}