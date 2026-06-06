from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Use parameterized queries to avoid command injection
    command = f'ping {shlex.quote(host)}'
    result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}