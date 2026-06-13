from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('$', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    escaped_host = escape_shell_arg(host)
    subprocess.run(["ping", escaped_host], check=True)
    return {"status": "completed"}