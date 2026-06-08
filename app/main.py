from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}