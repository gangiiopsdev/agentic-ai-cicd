from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    command = ['ping', safe_host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}