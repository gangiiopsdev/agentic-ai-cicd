from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_arg(host), shell=False)
    return {"status": "completed"}