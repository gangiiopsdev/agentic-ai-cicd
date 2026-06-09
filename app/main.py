from fastapi import FastAPI
import subprocess
import shlex
def is_safe_command(command: str) -> bool:
    return command.strip().lower() in ['ping', 'echo']
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not is_safe_command('ping') or not host:
        raise ValueError('Invalid or missing host')
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {'status': 'completed'}