from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host name')
    try:
        command = ['ping'] + shlex.split(escape_shell_arg(host))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}