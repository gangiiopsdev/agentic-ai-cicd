from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        host = shlex.quote(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)