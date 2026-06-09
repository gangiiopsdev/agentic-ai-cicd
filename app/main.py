from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host: str) -> bool:
    safe_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}