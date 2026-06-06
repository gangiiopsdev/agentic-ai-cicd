from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_host = escape_shell_arg(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)

    return {"status": "completed", "output": result.stdout}