from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    arg = str(arg)
    return ' '.join(map(shlex.quote, arg.split(' ')))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid characters in host name')
    escaped_host = escape_shell_arg(host)
    result = subprocess.run(['ping', *shlex.split(f'"{escaped_host}"')], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}