from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command_arg(arg):
    return shlex.quote(arg)

def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        subprocess.call(['ping', '--', escape_command_arg(host)])  # Add -- to prevent command injection
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}