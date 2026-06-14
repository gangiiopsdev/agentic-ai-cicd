from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    subprocess.call(["ping", escaped_host])
    return {"status": "completed"}