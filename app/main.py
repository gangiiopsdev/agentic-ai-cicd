from fastapi import FastAPI
import subprocess
import shlex
def escape_command(command: str) -> str:
    return command.replace(';', ' ').replace('&', ' ').replace('|', ' ').replace('$', '').replace('*', '')

class SafeSubprocess(subprocess.Popen):
    def __new__(cls, *args, **kwargs):
        if isinstance(args[0], list):
            args = (escape_command(arg) for arg in args[0])
        elif isinstance(args[0], str):
            args = (' '.join(escape_command(x) for x in shlex.split(args[0])),)
        return super().__new__(cls, *args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {'status': 'completed'}