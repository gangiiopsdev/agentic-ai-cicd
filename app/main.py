from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = quote(host, safe=':/')  # Ensure only allowed characters are passed to the command line
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}