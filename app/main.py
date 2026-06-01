from fastapi import FastAPI
import subprocess

class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

def escape_command_input(input_str):
    import shlex
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        SafeSubprocess.run(['ping', escape_command_input(host)], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400