from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_args(args):
    return [arg.replace(';', '').replace('&', '').replace('|', '') for arg in args]

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    subprocess.call(escape_shell_args(["ping", host]))
    return {"status": "completed"}