from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(subprocess.list2cmdline([arg]).split())

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}