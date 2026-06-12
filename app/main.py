from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
def escape_command_arg(arg):
    import shlex
    return shlex.quote(arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', escape_command_arg(host)], check=True, text=True)
    return {"status": "completed"}