from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input using shlex.quote to avoid shell injection
        output = subprocess.check_output(shlex.split(f'ping {shlex.quote(host)}'), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}