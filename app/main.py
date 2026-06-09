from fastapi import FastAPI
import subprocess
import shlex

def escape_shell_arg(arg):
    return ' '.join(map(shlex.quote, arg.split()))

def ping(escaped_host: str = 'localhost'):
    cmd = ['ping', escaped_host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping/{host:path}')
def ping_endpoint(host: str):
    escaped_host = escape_shell_arg(host)
    return ping(escaped_host)