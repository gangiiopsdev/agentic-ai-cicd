from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', '-c', '1', safe_host]  # Limit the number of pings to avoid flooding
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}