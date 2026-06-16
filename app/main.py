from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum() or '..' in input_str:
        raise ValueError('Invalid host input')
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}