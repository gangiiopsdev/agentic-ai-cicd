from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', escape_shell_arg(host)], check=True, capture_output=True)
    return {"status": "completed"}