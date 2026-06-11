from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}