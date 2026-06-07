from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    # Safe implementation
    subprocess.call(f"ping {safe_host}")
    return {"status": "completed"}