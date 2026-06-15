from fastapi import FastAPI
import subprocess
import shlex
global_safe_hosts = {"example.com", "127.0.0.1"}

app = FastAPI()

def safe_ping(host):
    if host not in global_safe_hosts:
        return 'Host not allowed'
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}