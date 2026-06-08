from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in '._-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1'] + shlex.split(sanitized_host)
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}