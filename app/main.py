from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host):
    try:
        output = subprocess.check_output(['ping'] + shlex.split(host), stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': _ping(host)}