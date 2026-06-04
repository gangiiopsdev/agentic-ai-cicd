from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    args = ['ping', '-c', '1', escaped_host]  # Use specific options for ping command to avoid shell interpretation
    subprocess.call(args, shell=False)
    return {'status': 'completed'}