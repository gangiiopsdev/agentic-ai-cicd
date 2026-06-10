from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

def escape_shell_argument(arg):
    return ''.join(shlex.quote(a) for a in arg.split())

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', escape_shell_argument(host)]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode(), 'error': result.stderr.decode()}