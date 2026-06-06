from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return ' '.join(map(shlex.quote, arg.split()))

@app.get('/ping')
def ping(escaped_host: str = 'localhost'):
    cmd = ['ping', escaped_host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}