from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command, *args):
    full_command = [command] + list(args)
    subprocess.call(full_command)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_subprocess_call("ping", shlex.quote(host))
    return {"status": "completed"}