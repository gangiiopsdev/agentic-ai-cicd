from fastapi import FastAPI
import subprocess
import shlex

class ShellEscapeError(Exception):
    pass

def escape_shell_arg(arg):
    try:
        return shlex.quote(arg)
    except Exception as e:
        raise ShellEscapeError(f'Failed to escape shell argument: {e}')

app = FastAPI()

def execute_ping(host: str):
    escaped_host = escape_shell_arg(host)
    try:
        subprocess.run(['ping', escaped_host], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    if 'error' in result:
        return result
    return {'status': 'completed'}