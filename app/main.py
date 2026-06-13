from fastapi import FastAPI
import subprocess
from typing import Dict
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Dict:
    # Secure implementation
    try:
        cmd = ['ping'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}