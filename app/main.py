from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    if host.isalnum():
        subprocess.call(['ping', '--', escape_command_arg(host)])  # Add -- to prevent command injection
    else:
        return {'status': 'invalid input'}
    return {'status': 'completed'}