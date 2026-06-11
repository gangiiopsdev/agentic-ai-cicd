from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host: str) -> str:
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', escaped_host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}