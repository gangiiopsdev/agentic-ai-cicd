from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in ('.', '-', '_'))
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {'status': 'completed'}