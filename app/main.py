from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}