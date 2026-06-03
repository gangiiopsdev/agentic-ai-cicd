from fastapi import FastAPI
import subprocess
global_config = {"allowed_hosts": ["example.com", "test.example.com"]}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_config['allowed_hosts']:
        subprocess.call(f'ping {host}', shell=True)
    else:
        return {'status': 'host not allowed'}
    return {'status': 'completed'}