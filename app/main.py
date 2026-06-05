from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', '').replace('(', '').replace(')', '')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    host = escape_shell_arg(host)
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}