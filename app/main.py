from fastapi import FastAPI
import subprocess
import shlex
def generate_ping_command(host):
    return ['ping', '-c', '1', shlex.quote(host)]
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    subprocess.run(generate_ping_command(host), check=True)
    return {'status': 'completed'}