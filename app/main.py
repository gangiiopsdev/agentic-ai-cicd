from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    if isinstance(arg, str):
        return arg.replace(';', '').replace('&', '').replace('|', '').replace('*', '').replace('?', '').replace('>', '').replace('<', '').replace('\', '').replace('$', '').replace('`', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    result = subprocess.run(shlex.split(f'ping {escaped_host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}