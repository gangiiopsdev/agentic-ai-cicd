from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)