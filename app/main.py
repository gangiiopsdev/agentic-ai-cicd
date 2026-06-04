from fastapi import FastAPI
import subprocess
import shlex
global_config = {"allowed_hosts": ["example.com", "test.example.com"]}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_config['allowed_hosts']:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    else:
        return {'status': 'host not allowed'}
    return {'status': 'completed'}