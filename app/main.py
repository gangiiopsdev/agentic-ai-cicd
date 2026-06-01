from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args):
        command_parts = shlex.split(command)
        full_command = [command_parts[0]] + list(map(shlex.quote, command_parts[1:] + list(args)))
        subprocess.call(full_command)

app = FastAPI()

def ping(host: str):
    if not all(char.isalnum() or char in ['.', '-'] for char in host):
        raise ValueError('Invalid hostname')
    SafeSubprocess.safe_call('ping', host)

@app.get('/ping')
def ping_route(host: str):
    return {'result': 'Pinging {}'.format(host)}