from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    cmd = ['ping', shlex.quote(sanitize_input(host))]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}