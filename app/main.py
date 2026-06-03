from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ').replace('$', ' ')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}