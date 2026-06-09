from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_args(args):
    return [arg.replace(';', '').replace('&', '').replace('|', '') for arg in args]

@app.get("/ping")
def ping(host: str):
    # Safer implementation with additional validation
    if not host or ' ' in host:
        raise ValueError("Invalid input")
    subprocess.call(escape_shell_args(["ping", host]))
    return {"status": "completed"}