from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    escaped_host = escape_shell_arg(host)
    subprocess.run(['ping', escaped_host], shell=False)
    return {"status": "completed"}