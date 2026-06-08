from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    # Safe implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}