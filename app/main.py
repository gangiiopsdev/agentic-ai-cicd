from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace('`', '\`').replace('$', '\$').replace('&', '\&')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', '-c 1', escaped_host])
    return {'status': 'completed'}