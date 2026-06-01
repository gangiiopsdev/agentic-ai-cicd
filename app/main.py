from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_args(args):
    return [shlex.quote(arg) for arg in args]

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_args(['ping', host]))
    return {"status": "completed"}