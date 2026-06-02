from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(escape_shell_arg(f"ping {host}"), shell=False, check=True)
    return {"status": "completed"}