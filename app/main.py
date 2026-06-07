from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import quote_plus

app = FastAPI()

def safe_ping(host):
    try:
        args = shlex.split('ping ' + quote_plus(host))
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}