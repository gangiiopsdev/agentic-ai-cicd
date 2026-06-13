from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

cmd = ['ping', quote(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}