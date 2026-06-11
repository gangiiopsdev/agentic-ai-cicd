from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f'ping {escape_shell_arg(host)}', shell=True)
    return {'status': 'completed'}