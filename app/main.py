from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg: str) -> str:
    return ''.join(c if c.isalnum() or c in "_.-:/" else f'\{ord(c):03o}' for c in arg)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    subprocess.call(f"ping {safe_host}")
    return {"status": "completed"}