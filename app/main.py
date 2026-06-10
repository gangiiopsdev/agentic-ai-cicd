from fastapi import FastAPI
import subprocess
import shlex

def escape_shell_arg(arg):
    return shlex.quote(arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid input for host")
    try:
        result = subprocess.run(["ping", escape_shell_arg(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}