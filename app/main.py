from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    result = subprocess.call(f"ping {escaped_host}")
    return {'status': 'completed'}