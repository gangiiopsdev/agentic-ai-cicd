from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    escaped_host = escape_shell_arg(host)
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}