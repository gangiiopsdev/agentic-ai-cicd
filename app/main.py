from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return ' '.join(shlex.quote(a) for a in arg.split())

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    escaped_host = escape_shell_arg(host)
    command = ['ping', escaped_host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}