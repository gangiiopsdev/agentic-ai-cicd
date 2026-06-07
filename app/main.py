from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def run_ping(host):
    # Secure implementation using subprocess.Popen and list for arguments
    args = ['ping', urlparse(host).hostname]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

@app.get("/ping")
def ping(host: str):
    output, error = run_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}