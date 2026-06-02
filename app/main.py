from fastapi import FastAPI
import subprocess
from shlex import quote
generate_safe_command = {'ping': ['ping', '{}']}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if host in generate_safe_command:
        safe_host = quote(host)
        command = generate_safe_command[host]
        subprocess.run(command, check=True, capture_output=True, text=True)
    else:
        raise ValueError('Unsafe input detected')
    return {'status': 'completed'}