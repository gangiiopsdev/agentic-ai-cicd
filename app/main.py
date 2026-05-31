from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(escape_shell_arg(f"ping {host}"))
    return {"status": "completed"}