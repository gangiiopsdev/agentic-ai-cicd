from fastapi import FastAPI
import subprocess
class ShellEscapeError(Exception):
    pass
def safe_subprocess(command: str, args: list):
    if any(arg.startswith('-') for arg in args):
        raise ShellEscapeError(f'Command {command} contains shell-escaped arguments.')
    subprocess.run([command] + [subprocess.escape(arg) for arg in args], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_subprocess('ping', [host])
    return {"status": "completed"}