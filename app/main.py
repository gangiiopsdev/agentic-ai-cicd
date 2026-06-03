from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg  # Remove the need for subprocess.list2cmdline as it's not necessary

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host name')
    try:
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to safely escape the host argument
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}