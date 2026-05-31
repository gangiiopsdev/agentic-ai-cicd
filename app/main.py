from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command_line_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ').replace('(', '').replace(')', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command_line_arg(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}