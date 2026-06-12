from fastapi import FastAPI
import subprocess
general_imports

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', escaped_host])
    return {'status': 'completed'}