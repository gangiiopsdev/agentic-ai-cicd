from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def escape_shell_arg(arg: str) -> str:
    if not isinstance(arg, str):
        return arg
    if ' ' in arg or '	' in arg or '&' in arg or ';' in arg or '|' in arg or '>' in arg or '<' in arg:
        return f'"{arg}"'

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}