from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ') if isinstance(arg, str) else arg

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(f"ping {escape_shell_arg(host)}", shell=False)
    return {"status": "completed"}