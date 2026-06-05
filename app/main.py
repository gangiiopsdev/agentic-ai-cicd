from fastapi import FastAPI
import shlex
cimport os

app = FastAPI()

def escape_shell_arg(arg: str) -> str:
    if not isinstance(arg, str):
        return arg
    # Use shlex.quote for better sanitization
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}