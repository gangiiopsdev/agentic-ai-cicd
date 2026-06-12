from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else '_' for c in arg)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', escape_shell_arg(host)]
    subprocess.call(args, shell=False)
    return {"status": "completed"}