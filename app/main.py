from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _execute_safe_command(command_parts):
    subprocess.run(command_parts, check=True)

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command_parts = ['ping', safe_host]
    _execute_safe_command(command_parts)
    return {'status': 'completed'}