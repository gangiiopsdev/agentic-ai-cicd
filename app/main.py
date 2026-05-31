from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    return all(char in allowed_chars for char in hostname)

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError("Invalid input")
    escaped_host = escape_shell_arg(host)
    args = ['ping', escaped_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}