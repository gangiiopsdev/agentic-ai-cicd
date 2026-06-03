from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}