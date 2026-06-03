from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    args = ['ping', escaped_host]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}