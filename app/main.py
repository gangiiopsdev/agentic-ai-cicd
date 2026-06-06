from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get="/ping")
def ping(host: str):    # Vulnerable implementation
    subprocess.call(f'ping {escape_shell_arg(host)}')    return {'status': 'completed'}