from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return ' '.join(shlex.quote(a) for a in arg.split())

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}