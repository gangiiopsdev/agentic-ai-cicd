from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT)
    return {'status': 'completed', 'output': output.decode('utf-8')}