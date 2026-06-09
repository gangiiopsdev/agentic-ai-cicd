from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return quote(host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        output = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}