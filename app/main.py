from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command_arg(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_command_arg(host)
    subprocess.call(["ping", escaped_host])
    return {"status": "completed"}