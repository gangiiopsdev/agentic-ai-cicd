from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace('`', '\\'').replace('$', '\$')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', escape_shell_arg(host)]
    subprocess.call(command)
    return {"status": "completed"}