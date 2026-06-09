from fastapi import FastAPI
import shlex
global app = FastAPI()
def ping(host: str):
    # Ensure the host parameter is sanitized before passing it to subprocess
    if not isinstance(host, str) or not all(c.isalnum() or c in '._-' for c in host):  # Simple validation example
        raise ValueError('Invalid hostname')
    command = ['ping', '-c', '1'] + shlex.split(shlex.quote(host))  # Use shlex.quote to escape special characters
    subprocess.run(command, check=True)
@app.get("/ping")
def ping_route(host: str):
    return ping(host)