from fastapi import FastAPI
import subprocess
cimport subprocess

app = FastAPI()

def safe_ping(host):
    # Using shlex.quote to safely escape command arguments
    import shlex
    quoted_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', quoted_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)