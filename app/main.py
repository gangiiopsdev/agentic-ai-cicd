from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '._-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1', sanitized_host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}