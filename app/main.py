from fastapi import FastAPI
import subprocess
from shlex import quote

def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use shlex.quote to ensure the command is safely quoted
    sanitized_host = quote(host)
    result = subprocess.run([os.path.abspath('/bin/ping'), sanitized_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}