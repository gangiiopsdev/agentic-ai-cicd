from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
def safe_subprocess_call(command, *args, **kwargs):
    import shlex
    command = shlex.split(command)
    subprocess.call(['ping', subprocess.list2cmdline([quote(sanitize_input(host))])], *args, **kwargs)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_subprocess_call(f'ping {host}')
    return {"status": "completed"}