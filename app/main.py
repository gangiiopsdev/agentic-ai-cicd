from fastapi import FastAPI
import subprocess

app = FastAPI()

def _safe_ping(host):
    safe_host = subprocess.list2cmdline([host])
    return ['ping', safe_host]

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(_safe_ping(host), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}