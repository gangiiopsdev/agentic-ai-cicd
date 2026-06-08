from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

global_env = {'host': ''}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, shell=False, env=global_env)