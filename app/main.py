from fastapi import FastAPI
import subprocess
import shlex
cimport = subprocess.run

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = cimport(f'ping {shlex.quote(host)}', capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}