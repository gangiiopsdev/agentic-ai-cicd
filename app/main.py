from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(shlex.quote(c) for c in arg.split())

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}