from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def escape_shell_arg(arg):
    return ' '.join(shlex.quote(a) for a in arg.split())

@app.get("/ping")
def ping(host: str):    # Vulnerable implementation
    subprocess.call(f'ping {escape_shell_arg(host)}')    return {'status': 'completed'}