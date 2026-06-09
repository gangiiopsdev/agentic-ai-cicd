from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import quote_plus

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = ['ping', quote_plus(host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output.decode('utf-8')}