from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    # Example validation logic, replace with actual validation
    return host.isalnum()

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    escaped_host = escape_shell_arg(host)
    command = ['ping', escaped_host]
    subprocess.run(command, check=True)  # Use subprocess.run instead of subprocess.call
    return {'status': 'completed'}