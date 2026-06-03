from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    host = escape_shell_arg(host)
    # Secure implementation using shell=False and list of arguments
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}