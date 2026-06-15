from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'output': result.stderr}
    return {'status': 'completed', 'output': result.stdout}