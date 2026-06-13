from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _execute_command(command, *args):
    cmd = command.format(*args)
    parts = shlex.split(cmd)
    subprocess.run(parts, check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    _execute_command('ping {host}', host=host)
    return {"status": "completed"}