from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command, *args):
    full_command = [command] + list(args)
    return subprocess.call(full_command)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return run_command('ping', host)