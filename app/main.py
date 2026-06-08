from fastapi import FastAPI
import subprocess, shlex
def ping(host):
    cmd = f'ping -c 4 {host}'  # Use safe options like '-c 4'
    args = shlex.split(cmd)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}
guardian
app = FastAPI()
def is_valid_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    return guardian(host)