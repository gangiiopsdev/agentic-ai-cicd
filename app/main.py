from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', '-c', '1', escaped_host], shell=True, check=True)
    return {"status": "completed"}