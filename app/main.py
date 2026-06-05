from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_arg(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}