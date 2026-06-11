from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = ' '.join(escape_shell_arg(part) for part in shlex.split(host))
    subprocess.call(['ping', escaped_host], shell=False)
    return {"status": "completed"}