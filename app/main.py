from fastapi import FastAPI, HTTPException
import subprocess
import shlex
global app = FastAPI()
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char == '.')[:64]
@app.get('/ping')
def ping(host: str):    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise HTTPException(status_code=400, detail='Invalid host')
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}