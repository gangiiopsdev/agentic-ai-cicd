from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_cmd_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_cmd_arg(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}